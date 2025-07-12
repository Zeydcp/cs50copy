describe("setup()", {
  it("has column names medal, country, gender", {
    expect_equal(colnames(setup()), c("medal", "country", "gender"))
  })
  it("has no missing values", {
    expect_equal(anyNA(setup()), FALSE)
  })
})