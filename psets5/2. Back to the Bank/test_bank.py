from bank import value


def main():
    test_hello()
    test_h()
    test_others()


def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("hello world") == 0
    assert value("Hello world") == 0


def test_h():
    assert value("Hi world") == 20
    assert value("haha world") == 20


def test_others():
    assert value("Namaste world") == 100
    assert value("I use arch btw :3 xD") == 100


if __name__ == "__main__":
    main()