cntry <- readline("Country: ")
file <- list()

for (number in 1:5) {
  file[[number]] <- read.csv(paste0("202", number-1, ".csv"))
  file[[number]] <- na.omit(file[[number]])

  if (cntry %in% unique(file[[number]]$country)) {
    file[[number]] <- subset(file[[number]], country == cntry)
    sum_happiness <- round(apply(file[[number]][, -1], MARGIN = 1, FUN = sum), digits = 2)
    cat(cntry, "(202", number-1, "): ", sum_happiness, "\n", sep = "")
  } else {
    cat(cntry, "(202", number-1, "): unavailable\n", sep = "")
  }

}




