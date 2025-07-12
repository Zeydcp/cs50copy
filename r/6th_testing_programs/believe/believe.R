# Load necessary libraries
library(stringr)

# Function to shift characters
shift_char <- function(char, shift) {
  # Handle lowercase letters
  if (char %in% letters) {
    return(letters[(match(char, letters) + shift - 1) %% 26 + 1])
  }

  # Handle uppercase letters
  if (char %in% LETTERS) {
    return(LETTERS[(match(char, LETTERS) + shift - 1) %% 26 + 1])
  }

  # Return special characters as they are
  return(char)
}

# Main function to encrypt string
encrypt_string <- function(input_string) {
  # Input validation
  if (is.nan(input_string)) {
    warning("NaN detected; no encryption performed.") # Issue warning for NaN
    return(input_string) # Return original input
  }
  if (is.na(input_string)) {
    stop("Input cannot be NA.") # Throw error for NA
  }
  if (is.infinite(input_string)) {
    warning("Infinite value detected; no encryption performed.") # Issue warning for Inf and -Inf
    return(input_string) # Return original input
  }
  if (!is.character(input_string)) {
    stop("Input must be a string.") # Throw error for non-string inputs
  }
  # Split the string into words
  words <- str_split(input_string, " ")[[1]]

  # Get the lengths of the words
  word_lengths <- str_length(words)

  # Calculate alternating sum and multiplication
  result <- word_lengths[1] # Start with the first length
  if (length(word_lengths) > 1) {
    for (i in 2:length(word_lengths)) {
      if (i %% 2 == 0) {
        result <- result + word_lengths[i] # Add on even indexes
      } else {
        result <- result * word_lengths[i] # Multiply on odd indexes
      }
    }
  }

  # If the result exceeds 25, cycle it back using modulo
  shift_value <- result %% 26

  # Convert the string into a vector of characters
  char_vector <- str_split(input_string, "")[[1]]

  # Apply Caesar cipher shift to each character
  encrypted_chars <- sapply(char_vector, shift_char, shift = shift_value)

  # Collapse the encrypted characters back into a string
  encrypted_string <- paste0(encrypted_chars, collapse = "")

  return(encrypted_string)
}