from twttr import shorten

def test_capitals():
    assert shorten("COOPER") == "CPR"
    assert shorten("RACER") == "RCR"
    assert shorten("FANTASTIC") == "FNTSTC"


def test_lowers():
    assert shorten("after") == "ftr"
    assert shorten("hey") == "hy"
    assert shorten("codify") == "cdfy"


def test_numbers():
    assert shorten("50") == "50"
    assert shorten("23") == "23"
    assert shorten("1009") == "1009"


def test_punctuation():
    assert shorten("!?") == "!?"
    assert shorten("*/%") == "*/%"
    assert shorten("£=") == "£="