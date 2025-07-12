library(tidyverse)

load("zelda.RData")

zelda <- zelda |>
  filter(grepl("Shigeru Miyamoto", producers)) |>
  group_by(title) |>
  slice_min(order_by = year) |>
  ungroup() |>
  arrange(year, title, system)

save(zelda, file="4.RData")