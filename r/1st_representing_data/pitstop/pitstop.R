filename <- readline("Enter a CSV file: ")

file <- read.csv(filename)

print(nrow(file))
print(min(file$time))
print(max(file$time))
print(sum(file$time))