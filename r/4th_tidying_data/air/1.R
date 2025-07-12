library(tidyverse)

air <- read.csv("air.csv") |>
  as_tibble()

air <- air |>
  select(State,
         State.County,
         POLLUTANT,
         Emissions..Tons.,
         starts_with("SCC.LEVEL.")) |>

  rename(state=State,
         county=State.County,
         pollutant=POLLUTANT,
         emissions=Emissions..Tons.) |>

  rename_with(~ sub("SCC.LEVEL.", "level_", .x))

air$county <- air$county |>
  str_replace_all("OR - ", "")

air$emissions <- air$emissions |>
  str_replace_all(",", "")

save(air, file="air.RData")
