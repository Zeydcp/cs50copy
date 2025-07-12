describe("prompt()", {
  it("returns correct column based on response", {
    expect_equal(colnames(prompt(response = 1, answer = c("spain", "Male")))[1], "medal")
    expect_equal(colnames(prompt(response = 2, answer = c("gold", "FEMALE")))[1], "country")
    expect_equal(colnames(prompt(response = 3, answer = c("bronze", "united States")))[1], "gender")
  })
  it("returns correct number of table rows for gender", {
    expect_equal(nrow(prompt(response = 3, answer = c("Gold", "spain"))), 2)
  })
})