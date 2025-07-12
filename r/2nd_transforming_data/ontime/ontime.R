rail <- read.csv("rail.csv")
bus <- read.csv("bus.csv")

input_route <- readline("Route: ")

if (input_route %in% unique(rail$route)) {
  dataset <- rail
} else if (input_route %in% unique(bus$route)) {
  dataset <- bus
}

if (exists("dataset")) {
  avg_peak <- round(mean(
    subset(
      dataset,
      route == input_route & peak == "PEAK")$numerator/subset(
        dataset,
        route == input_route & peak == "PEAK")$denominator)*100)

  avg_offpeak <- round(mean(
    subset(
      dataset,
      route == input_route & peak == "OFF_PEAK")$numerator/subset(
        dataset,
        route == input_route & peak == "OFF_PEAK")$denominator)*100)

  cat("On time", paste0(avg_peak, "% of the time during peak hours.\n"))
  cat("On time", paste0(avg_offpeak, "% of the time during off-peak hours.\n"))
} else {
  print("Enter a valid route")
}