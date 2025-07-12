library(tidyverse)

load("air.RData")

air <- air |>
  filter(county == "Multnomah")

save(air, file="3.RData")
