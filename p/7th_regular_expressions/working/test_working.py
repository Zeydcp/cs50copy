from working import convert
from pytest import raises


def test_different_format():
    with raises(ValueError):
        convert("12:09 PM - 6:16 AM")
    with raises(ValueError):
        convert("4:08 PM 6:41 PM")


def test_single_format():
    assert convert("12 AM to 6 AM") == "00:00 to 06:00"
    assert convert("10 PM to 10 AM") == "22:00 to 10:00"
    with raises(ValueError):
        convert("25 PM to 8 PM")
    with raises(ValueError):
        convert("0 PM to 8 PM")


def test_double_format():
    assert convert("12:09 PM to 6:25 AM") == "12:09 to 06:25"
    assert convert("10:00 PM to 10:15 AM") == "22:00 to 10:15"
    with raises(ValueError):
        convert("12:60 PM to 8:12 PM")
    with raises(ValueError):
        convert("12:10 PM to 13:12 PM")
