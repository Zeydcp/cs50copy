from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
list = figlet.getFonts()
argv = sys.argv

if len(argv) == 1:
    f = random.choice(list)
elif len(argv) == 3 and (argv[1] == "-f" or argv[1] == "--font") and argv[2] in list:
    f = argv[2]
else:
    sys.exit("Invalid usage")

figlet.setFont(font=f)
answer = input("Input: ")
print("Output: \n" + figlet.renderText(answer))
