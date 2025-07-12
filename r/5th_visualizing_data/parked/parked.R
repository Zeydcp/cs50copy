library(tidyverse)

song <- read_file("lyrics/astley.txt")

table <- song |>
  str_replace_all("[\\n\\-]", " ") |>
  str_remove_all("[\\(\\),]") |>
  str_to_title() |>
  str_squish() |>
  str_split(pattern = " ") |>
  data.frame()

colnames(table) <- "words"
table <- table |>
  group_by(words) |>
  summarize(count = n()) |>
  ungroup() |>
  filter(count > 4) |>
  arrange(desc(count))

table$words <- factor(table$words, levels = table$words)

p <- ggplot(table, aes(x = words, y = count)) +
  geom_col(aes(fill = words), show.legend=FALSE) +
  labs(
    x = "Words",
    y = "Count"
  ) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))


ggsave(
  "lyrics.png",
  plot = p,
  width = 2000,
  height = 920,
  units = "px"
)
