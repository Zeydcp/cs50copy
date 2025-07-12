library(tidyverse)

zelda <- read.csv("zelda.csv") |>
  as_tibble()

zelda <- zelda |>
  separate(release,
           c("year", "system"),
           sep="\\s-\\s") |>
  pivot_wider(names_from = role,
              values_from = names) |>
  rename_with(tolower)

save(zelda, file="zelda.RData")
