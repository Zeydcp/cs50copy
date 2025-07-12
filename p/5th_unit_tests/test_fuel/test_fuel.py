from fuel import convert, gauge
from pytest import raises


def test_convert_zero_negative():
    with raises(ValueError):
        convert("0/-5")
    with raises(ZeroDivisionError):
        convert("7/0")


def test_convert():
    assert convert("4/5") == 80
    with raises(ValueError):
        convert("5/4")
    with raises(ValueError):
        convert("cat/mouse")


def test_gauge_negative():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(6) == "6%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"