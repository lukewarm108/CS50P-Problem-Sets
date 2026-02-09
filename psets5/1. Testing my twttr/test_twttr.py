from twttr import shorten

def main():
    test_shorten()


def test_shorten():
    assert shorten("Twitter!") == "Twttr!"
    assert shorten("xaeioux?") == "xx?"
    assert shorten("xAEIOUx,") == "xx,"
    assert shorten("CS50.") == "CS50."


if __name__ == "__main__":
    main()