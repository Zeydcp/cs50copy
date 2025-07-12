library(tidyverse)

load("air.RData")
air$emissions <- as.numeric(air$emissions)

air <- air |>
  filter(county == "Multnomah") |>
  arrange(desc(emissions))

save(air, file="4.RData")
