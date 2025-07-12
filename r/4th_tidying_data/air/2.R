library(tidyverse)

load("air.RData")
air$emissions <- as.numeric(air$emissions)

air <- air |>
  arrange(desc(emissions))

save(air, file="2.RData")
