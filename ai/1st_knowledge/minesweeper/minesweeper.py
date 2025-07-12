import itertools
import random
from random import choice


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        if len(self.cells) != 0 and len(self.cells) == self.count:
            return self.cells
        else:
            return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if len(self.cells) != 0 and self.count == 0:
            return self.cells
        else:
            return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

        self.updated_knowledge = True

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def sub_small_from_big(self, sentence1: Sentence, sentence2: Sentence) -> Sentence:
        if len(sentence1.cells) > len(sentence2.cells):
            return Sentence(sentence1.cells.difference(sentence2.cells), sentence1.count - sentence2.count)
        else:
            return Sentence(sentence2.cells.difference(sentence1.cells), sentence2.count - sentence1.count)

    def helper_function(self, new_sentence: Sentence):
        empty = Sentence(set(), 0)

        mines_intersect = self.mines.intersection(new_sentence.cells)
        safes_intersect = self.safes.intersection(new_sentence.cells)

        for mine in mines_intersect:
            new_sentence.mark_mine(mine)
        for safe in safes_intersect:
            new_sentence.mark_safe(safe)

        # Add sentence to KB
        if new_sentence.known_mines():
            self.updated_knowledge = True
            for cell in new_sentence.cells.copy():
                self.mark_mine(cell)

        elif new_sentence.known_safes():
            self.updated_knowledge = True
            for cell in new_sentence.cells.copy():
                self.mark_safe(cell)

        elif new_sentence not in self.knowledge and new_sentence != empty:
            self.updated_knowledge = True
            self.knowledge.append(new_sentence)

        while empty in self.knowledge:
            self.knowledge.remove(empty)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        self.moves_made.add(cell)

        if cell not in self.safes:
            self.mark_safe(cell)

        cells = []

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell or (i, j) in self.safes:
                    continue

                if (i, j) in self.mines:
                    count -= 1
                    continue

                # Add current cell to list of cells
                if 0 <= i < self.height and 0 <= j < self.width:
                    cells.append((i, j))

        # Draft sentence
        new_sentence = Sentence(cells, count)

        self.helper_function(new_sentence=new_sentence)

        while self.updated_knowledge:
            self.updated_knowledge = False
            knowledge_base: list[Sentence] = self.knowledge.copy()

            if len(knowledge_base):
                self.helper_function(new_sentence=knowledge_base[0])

            for i in range(len(knowledge_base)-1):

                for j in range(i+1, len(knowledge_base)):

                    if i == 0:
                        self.helper_function(new_sentence=knowledge_base[j])

                    # If any previous sentence is a subset or superset of the new one, remove overlap from new sentence
                    if (knowledge_base[i].cells.issubset(knowledge_base[j].cells) or knowledge_base[i].cells.issuperset(knowledge_base[j].cells)) and knowledge_base[i].cells and knowledge_base[j].cells:

                        if knowledge_base[i] == knowledge_base[j]:
                            self.knowledge.remove(knowledge_base[i])

                        new_sentence = self.sub_small_from_big(knowledge_base[i], knowledge_base[j])

                        self.helper_function(new_sentence=new_sentence)

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        safe_unmade = self.safes - self.moves_made
        for safe in safe_unmade:
            return safe

        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        full_board = {(i, j) for i in range(self.height) for j in range(self.width)}
        seperate = full_board.difference(self.moves_made.union(self.mines))

        if len(seperate) == 0:
            return None

        i, j = choice(list(seperate))

        return (i, j)
