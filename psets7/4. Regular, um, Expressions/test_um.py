from um import count

def main():
    test_sent()
    test_punc()
    test_words()

def test_sent():
    assert count("um, sybau") == 1
    assert count("um, sygau, um, haha") == 2
    assert count("are you-um-gay?") == 1

def test_punc():
    assert count("-um-") == 1
    assert count("um-um-um") == 3

def test_words():
    assert count("uhmm") == 0
    assert count("umum") == 0
    assert count("um") == 1
    assert count("Um uM UM") == 3