visualize <- function() {

  table <- prompt()
  table[[1]] <- factor(table[[1]], levels = table[[1]])

  p <- ggplot(table, aes(x = eval(parse(text = colnames(table)[1])), y = count)) +
    geom_col(aes(fill = eval(parse(text = colnames(table)[1]))), show.legend=FALSE) +
    labs(
      x = str_to_title(colnames(table[1])),
      y = "Count"
    ) +
    theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))


  ggsave(
    "olympics.png",
    plot = p,
    width = 2000,
    height = 920,
    units = "px"
  )
  return (p)
}