random_character <- function() {
  # TODO: Return one random letter
  sample(letters, 1)
}

print_sequence <- function(length) {
  # TODO: Print a random sequence of specified length
  for (i in 1:length) {
    cat(random_character())
    Sys.sleep(0.25)
  }
}

print_sequence(20)
