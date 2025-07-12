flavor <- readline("Flavor: ")

caffeine <- readline("Caffeine: ")

if (flavor == "Light" && caffeine == "No") {
  print("chamomile tea")
} else if (flavor == "Light" && caffeine == "Yes") {
  print("green tea")
} else if (flavor == "Bold" && caffeine == "No") {
  print("rooibos tea")
} else if (flavor == "Bold" && caffeine == "Yes") {
  print("black tea")
}
