library(tidyverse)

load("air.RData")
air$emissions <- as.numeric(air$emissions)

air <- air |>
  group_by(county) |>
  slice_max(emissions) |>
  ungroup()


save(air, file="5.RData")
