from seasons import minutes_alive, in_words
from pytest import raises


def test_minutes_alive():
    assert minutes_alive("2023-10-02") == 1440
    assert minutes_alive("2023-10-01") == 2880
    with raises(ValueError):
        minutes_alive("2006-13-07")
    with raises(ValueError):
        minutes_alive("2006-11-31")


def test_in_words():
    assert in_words(100) == "One hundred minutes"
    assert in_words(1250) == "One thousand, two hundred fifty minutes"
    assert in_words("1250") == "One thousand, two hundred fifty minutes"
