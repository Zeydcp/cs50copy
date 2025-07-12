library(tidyverse)
library(ggplot2)

mcud <- read.csv("mcud.csv")

mcud <- mcud |>
  rename_with(tolower) |>
  rename(year = period,
         Line = marriages_or_divorces)

p <- ggplot(mcud, aes(x = year, y = count, color = Line)) +
  geom_line() +
  geom_point() +
  scale_y_continuous(limits = c(0, 25000)) +
  labs(
    x = "Year",
    y = "Occurence"
  )

ggsave(
  "visualization.png",
  plot = p,
  width = 2000,
  height = 920,
  units = "px"
)


