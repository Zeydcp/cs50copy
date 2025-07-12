setup <- function() {
  library(tidyverse)
  library(devtools)
  library(testthat)


  medalists <- read.csv("/workspaces/93766403/r/project/olympics/medalists.csv")

  medalists <- medalists |>
    select(medal,
           country_medal,
           sex_or_gender) |>
    rename(country = country_medal,
           gender = sex_or_gender) |>
    na.omit() |>
    sapply(str_to_title) |>
    data.frame()

  medalists$country <- str_replace_all(medalists$country,
                                       "( Of America)|(People's Republic Of )",
                                       "")
  return (medalists)
}

