library(tidyverse)

load("zelda.RData")

zelda <- zelda |>
  filter(grepl(",\\s", producers)) |>
  group_by(title) |>
  slice_min(order_by = year) |>
  ungroup() |>
  arrange(year, title, system)

save(zelda, file="5.RData")