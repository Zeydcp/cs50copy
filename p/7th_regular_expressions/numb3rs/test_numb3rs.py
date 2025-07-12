from numb3rs import validate

def test_letters():
    assert validate("cat") == False
    assert validate("five.six.ten.seventy") == False

def test_digits():
    assert validate("127.89.0.256") == False
    assert validate("127.89.0.255") == True
    assert validate("0.0.0.0") == True
    assert validate("-1.89.0.-9") == False
    assert validate("89.0.9") == False
    assert validate(".89.0.9") == False
    assert validate("1.89..9") == False