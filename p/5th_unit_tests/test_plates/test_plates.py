from plates import is_valid

def test_capitals():
    assert is_valid("ABCGHHH") == False
    assert is_valid("BBJIO") == True


def test_lowers():
    assert is_valid("abcghhh") == False
    assert is_valid("bbjio") == True


def test_numbers():
    assert is_valid("650") == False
    assert is_valid("CS50") == True
    assert is_valid("HEL50L") == False
    assert is_valid("HEL05") == False


def test_punctuation():
    assert is_valid("RG*/?!") == False
    assert is_valid("TS%^&") == False

def test_punctuation():
    assert is_valid("RG*/?!") == False
    assert is_valid("TS%^&") == False