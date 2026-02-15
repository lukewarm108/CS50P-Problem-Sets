import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg1_ext = os.path.splitext(arg1)[1].lower()
    arg2_ext = os.path.splitext(arg2)[1].lower()
    valid_ext = [".jpg", ".jpeg", ".png"]
    if arg1_ext not in valid_ext or arg2_ext not in valid_ext:
        sys.exit("Invalid input")
    elif arg1_ext != arg2_ext:
        sys.exit("Input and output have different extensions")

    try:
        photo = Image.open(arg1)
    except FileNotFoundError:
        sys.exit("Input file does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = ImageOps.fit(photo, size)
    photo.paste(shirt, shirt)
    
    photo.save(arg2)


if __name__ == "__main__":
    main()