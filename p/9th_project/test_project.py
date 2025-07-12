from p.project.project import (
    choice_function,
    get_amount,
    user_confirmer,
    password_confirmer,
    verify_login,
    add_amount,
    sub_amount,
)
from pytest import raises


def test_choice_function():
    assert choice_function(6, 6) == 6
    assert choice_function(1, 4) == 1

    with raises(ValueError):
        choice_function(6, 5)
    with raises(ValueError):
        choice_function("5", 6)
    with raises(ValueError):
        choice_function(0, 6)
    with raises(ValueError):
        choice_function(-2, 6)


def test_get_amount():
    assert get_amount("17.4") == 17.4
    assert get_amount("12.67") == 12.67

    with raises(TypeError):
        get_amount(15)
    with raises(ValueError):
        get_amount("13.005")
    with raises(ValueError):
        get_amount("cat")
    with raises(ValueError):
        get_amount("-17")


def test_user_confirmer():
    assert user_confirmer("b") == "b"
    assert user_confirmer("St4rD3str0y3r") == "St4rD3str0y3r"

    with raises(ValueError):
        user_confirmer("a")
    with raises(ValueError):
        user_confirmer("a!")
    with raises(ValueError):
        user_confirmer("a b")


def test_password_confirmer():
    assert password_confirmer("b", "b") == "b"
    assert password_confirmer("a!3?", "a!3?") == "a!3?"

    with raises(ValueError):
        password_confirmer("a b", "a b")
    with raises(ValueError):
        password_confirmer("ab", "ba")


def test_verify_login():
    assert verify_login("a", "a") == (
        ("User", "a"),
        ("Balance", "${:,.2f}".format(100)),
        (1, "Add cash"),
        (2, "Withdraw cash"),
        (3, "Log Out"),
    )
    assert verify_login("bronze", "one") == (
        ("User", "bronze"),
        ("Balance", "${:,.2f}".format(0)),
        (1, "Add cash"),
        (2, "Withdraw cash"),
        (3, "Log Out"),
    )

    with raises(ValueError):
        verify_login("b", "a")
    with raises(ValueError):
        verify_login("bronze", "two")
    with raises(ValueError):
        verify_login("b", "b")


def test_add_amount():
    add_amount("a", 100)
    assert verify_login("a", "a")[1][1] == "${:,.2f}".format(200)


def test_sub_amount():
    sub_amount("a", 100)
    assert verify_login("a", "a")[1][1] == "${:,.2f}".format(100)
