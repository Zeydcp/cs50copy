from um import count


def test_case_input():
    assert count("Um hey, um") == 2
    assert count("Um yUM") == 1


def test_um_words():
    assert count("yummy") == 0
    assert count("bum, hi") == 0


def test_occurences():
    assert count("um um, um!") == 3
    assert count("summary of um my life") == 1