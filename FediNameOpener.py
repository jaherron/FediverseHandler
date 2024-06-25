import sys
import webbrowser

inputname = ""
if len(sys.argv)>1:
    inputname=sys.argv[1]
else:
    print("No input provided.")
    exit()

splitinput = inputname.split("@")

link = "https://"+splitinput[2]+"/@"+splitinput[1]

webbrowser.open(link)