library(tidyverse)

load("air.RData")

air <- air |>
  select(pollutant,
         emissions,
         level_1) |>
  rename(source=level_1)

air <- air[, c("source", "pollutant", "emissions")]

air$emissions <- as.numeric(air$emissions)

air <- air |>
  group_by(source,
           pollutant) |>
  summarize(emissions = sum(emissions)) |>
  ungroup() |>
  arrange(source,
          pollutant)

save(air, file="7.RData")


