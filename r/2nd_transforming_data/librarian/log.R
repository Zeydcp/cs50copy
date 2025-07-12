# Collecting books in csv
books <- read.csv("books.csv")

# Filtering out any rows that don't have author Mia Morgan
writer <- subset(books, author == "Mia Morgan")$title
print(writer)

# Filtering out any rows that don't have year 1613 and topic of Music
musician <- subset(books, year == 1613 & topic == "Music")$title
print(musician)

# Filtering out any rows that don't have year 1775 and author Lysandra Silverleaf or Elena Petrova
traveler <- subset(books,
                   year == 1775 & author %in% c("Lysandra Silverleaf", "Elena Petrova"))$title
print(traveler)

# Filtering out any rows that don't have year 1990 or 1992 and 200-300 pages
painter <- subset(books,
                   year %in% c(1990, 1992) & 200 < pages & pages < 300)$title
print(painter)

# Filtering out any rows that don't have "Quantum Mechanics" in the title
scientist <- subset(books, grepl("Quantum Mechanics", title))$title
print(scientist)

# Collecting authors in csv
authors <- read.csv("authors.csv")

# Filter for authors from Zenthia
authors <- subset(authors, hometown == "Zenthia")$author

# Filtering out any rows that aren't in 1700s and author not from Zenthia
teacher <- subset(books, 1699 < year & year < 1800 & author %in% authors)$title
print(teacher)