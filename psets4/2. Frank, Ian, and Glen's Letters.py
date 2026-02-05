from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        usr_font = sys.argv[2]
        if usr_font in fonts:
            figlet.setFont(font=usr_font)
        else: sys.exit("Not a valid font.")
    else: sys.exit("Use '-f' or '--font' to choose a font.")
elif len(sys.argv) > 3 or len(sys.argv) == 2:
    sys.exit("There must be either two valid arguements or none at all.")
else:
    print("A random font will be selected for you. In order to select a font of your choice, use '-f' or '--font' flag followed by a valid font name.\n")
    figlet.setFont(font=random.choice(fonts))

text = input("Input: ")
print(figlet.renderText(text))