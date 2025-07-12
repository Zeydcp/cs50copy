from bank import value

def test_capitals():
    assert value("HELLO") == 0
    assert value("HEY PAL") == 20
    assert value("YOOOO") == 100


def test_lowers():
    assert value("hello") == 0
    assert value("hey pal") == 20
    assert value("yoooo") == 100


def test_numbers():
    assert value("hello50") == 0
    assert value("h3y pal") == 20
    assert value("y0000") == 100


def test_punctuation():
    assert value("hello!") == 0
    assert value("hey pal?") == 20
    assert value("y*&*") == 100