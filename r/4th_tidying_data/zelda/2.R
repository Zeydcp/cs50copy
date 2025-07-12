library(tidyverse)

load("zelda.RData")

zelda <- zelda |>
  group_by(year) |>
  summarize(releases = n()) |>
  ungroup() |>
  arrange(desc(releases))

save(zelda, file="2.RData")
