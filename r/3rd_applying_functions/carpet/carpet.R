calculate_growth_rate <- function(years, visitors) {
  # TODO: Calculate yearly growth of visitors
  return((tail(visitors, 1)-visitors[1]) / (tail(years, 1)-years[1]))
}

predict_visitors <- function(years, visitors, year) {
  # TODO: Predict visitors in given year
  growth_rate <- calculate_growth_rate(years, visitors)
  return(tail(visitors, 1) + (growth_rate * (year-tail(years, 1))))
}

visitors <- read.csv("visitors.csv")
year <- as.integer(readline("Year: "))
predicted_visitors <- predict_visitors(visitors$year, visitors$visitors, year)
cat(paste0(predicted_visitors, " million visitors\n"))
