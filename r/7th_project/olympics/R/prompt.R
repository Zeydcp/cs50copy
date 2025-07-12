prompt <- function(response = NA, answer = NA) {
  df <- setup()

  cols <- colnames(df)

  if (anyNA(c(response, answer))) {
    response <- cols |>
      str_to_title() |>
      paste("Analysis") |>
      menu()

    question <- cols[-response]
    df2 <- df[-response]
    answer <- c()

    for (i in seq_along(question)) {
      while (TRUE) {
        potential_answer <- question[i] |>
            str_to_title() |>
            paste0(": ") |>
            readline() |>
            str_to_title()

        if (potential_answer %in% unique(df2[, i])) {
          answer <- append(answer, potential_answer)
          break
        } else {
          cat("Enter a valid ", question[i], ".", sep = "")
        }
      }
    }

    df <- filter(df,
                 eval(parse(text = question[1])) == answer[1] &
                 eval(parse(text = question[2])) == answer[2]
                 )
  } else {
    answer <- sapply(answer, str_to_title)
    question <- cols[-response]
    df <- filter(df,
                 eval(parse(text = question[1])) == answer[1] &
                 eval(parse(text = question[2])) == answer[2]
          )
  }

  if (cols[response] == "medal") {
    df <- group_by(df, medal)
  } else if (cols[response] == "country") {
    df <- group_by(df, country)
  } else {
    df <- group_by(df, gender)
  }

  df <- df[response] |>
    summarize(count = n()) |>
    ungroup() |>
    arrange(desc(count))

}