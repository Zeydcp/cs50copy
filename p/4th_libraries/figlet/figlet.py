from sys import exit, argv
from random import choice
from pyfiglet import Figlet

argl = len(argv)
if argl not in [1, 3]:
    exit("Invalid usage")

figlet = Figlet()
font_list = figlet.getFonts()

try:
    if argv[1] not in ["-f", "--font"] or argv[2] not in font_list:
        exit("Invalid usage")
except IndexError:
    pass

if argl == 1:
    chosen = choice(font_list)
    figlet.setFont(font=chosen)
else:
    figlet.setFont(font=argv[2])

output = input("Input: ")
print("Output:\n\n" + figlet.renderText(output))
