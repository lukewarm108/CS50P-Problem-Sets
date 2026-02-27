from seasons import convert
from datetime import date, timedelta
import pytest


def test_format():
    with pytest.raises(SystemExit):
        convert("hello")
    with pytest.raises(SystemExit):
        convert("01-01-2000")
    with pytest.raises(SystemExit):
        convert("2000/01/01")


def test_future():
    tomorrow = (date.today() + timedelta(days=1)).isoformat()
    with pytest.raises(SystemExit):
        convert(tomorrow)


def test_today():
    today = date.today().isoformat()
    assert convert(today) == "Zero minutes"