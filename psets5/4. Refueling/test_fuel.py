from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()


def test_convert():
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("2/3") == 67
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"

if __name__ == "__main__":
    main()