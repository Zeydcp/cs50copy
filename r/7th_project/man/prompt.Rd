\name{prompt}
\alias{prompt}
\title{prompt}
\description{Prompts the user for either a medal, country, or gender analysis of the 2024 olympics medal winners, then depending on your analysis it will prompt you for answers to the 2 other fields to isolate the variable you're looking to analyze}
\usage{
prompt()
prompt(response = 1, answer = c("spain", "MALE"))
}
\arguments{
\item{response}{
    A numeric value ranging from 1-3.
  }
  \item{answer}{
    A string vector of length 2 containing the answers to 2 of medal level, country, and gender.
  }
}
\value{
A data frame of 2 columns containing the count of the analysis you selected for.
}
\examples{
View(prompt())
}