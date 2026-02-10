from plates import is_valid

def main():
    test_length()
    test_alnum()
    test_startletters()
    test_digit()


def test_length():
    assert is_valid("AB") == True
    assert is_valid("ABC123") == True
    assert is_valid("A") == False
    assert is_valid("1") == False
    assert is_valid("ABCD123") == False


def test_alnum():
    assert is_valid("ABC 12") == False
    assert is_valid("ABC.12") == False


def test_startletters():
    assert is_valid("ABC12") == True
    assert is_valid("A211") == False


def test_digit():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA012") == False


if __name__ == "__main__":
    main()