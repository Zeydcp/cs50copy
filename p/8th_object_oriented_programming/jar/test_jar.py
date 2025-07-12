from jar import Jar
from pytest import raises


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar.__init__(0)
    assert jar.capacity == 0
    with raises(ValueError):
        jar.__init__(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    with raises(ValueError):
        jar.deposit(11)


def test_withdraw():
    jar = Jar()
    with raises(ValueError):
        jar.withdraw(1)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
