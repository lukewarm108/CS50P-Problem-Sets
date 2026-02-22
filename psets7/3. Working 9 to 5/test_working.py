from working import convert
import pytest

def main():
    test_value()
    test_hour()
    test_min()

def test_value():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("8AM9PM")

def test_hour():
    assert convert("9 AM to 3 PM") == "09:00 to 15:00"
    assert convert("5 PM to 6 AM") == "17:00 to 06:00"
    with pytest.raises(ValueError):
        convert("13 PM to 15 AM")

def test_min():
    assert convert("9:14 AM to 8:30 PM") == "09:14 to 20:30"
    with pytest.raises(ValueError):
        convert("9:60 AM to 12:102 PM")