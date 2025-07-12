library(stringr)
library(testthat)

test_that("`str_length` finds regular string length", {
  expect_equal(str_length("abc"), 3)
  expect_equal(str_length("Hello"), 5)
  expect_equal(str_length(""), 0)
})

test_that("`str_length` finds non-alphabetic string length", {
  expect_equal(str_length("12"), 2)
  expect_equal(str_length("  "), 2)
  expect_equal(str_length("Hey!"), 4)
  expect_equal(str_length("Hey 😂"), 5)
})

test_that("`str_length` treats special characters as strings", {
  expect_equal(str_length(NA), NA_integer_)
  expect_equal(str_length(NaN), 3)
  expect_equal(str_length(Inf), 3)
  expect_equal(str_length(-Inf), 4)
})

test_that("`str_length` handles each value in vectors and data frames separately", {
  expect_equal(str_length(c("1", "2")), c(1, 1))
  expect_warning(str_length(data.frame(1:3, 2)))
})

