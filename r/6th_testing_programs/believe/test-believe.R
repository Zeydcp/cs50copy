library(testthat)

source("believe.R")

test_that("`encrypt_string` returns encrypted version of string", {
  expect_equal(encrypt_string("Hi"), "Jk")
  expect_equal(encrypt_string("Hi there pal"), "Cd oczmz kvg")
  expect_equal(encrypt_string("how are you"), "zgo sjw qgm")
})

test_that("`encrypt_string` doesn't encrypt non-alphabetic characters", {
  expect_equal(encrypt_string("Yo!"), "Br!")
  expect_equal(encrypt_string("I went to eat food 😂"), "J xfou up fbu gppe 😂")
})

test_that("`encrypt_string` returns error for NA and warnings for other special characters", {
  expect_error(encrypt_string(NA))
  expect_warning(encrypt_string(NaN))
  expect_warning(encrypt_string(Inf))
  expect_warning(encrypt_string(-Inf))
})

test_that("`encrypt_string` returns error for vectors and data frames", {
  expect_error(encrypt_string(1:3))
  expect_error(encrypt_string(data.frame(1:3, 2, 3)))
})