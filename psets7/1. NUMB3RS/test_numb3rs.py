from numb3rs import validate


def main():
    test_octet()
    test_number()

def test_moreoctet():
    assert validate("123.32.23.43.2") == False
    assert validate("123.32.23.43") == True
    assert validate("32.12.42") == False

def test_number():
    assert validate("256.12.12.32") == False
    assert validate("255.12.3.22") == True
    assert validate("0.32.31.12") == True
    assert validate("123.1243.1235.555") == False
    assert validate("Hello") == False