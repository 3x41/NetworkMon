import sys
import os

# insert at 1, 0 is the script path (or '' in REPL)

def Main_Menu():
    print ("Welcome to Network Monitor\n")
    print ("    1. Run the Poller")
    print ("    2. Run the Program")
    print ("    3. Exit Program")
    
while 1:
    Main_Menu()
    Result = input("\nEnter a number option and press enter : ")

    if Result == "1":
        print ("Running Poller")
        #import Poller
        os.system("python Bin/Poller.py")
    elif Result == "2":
        print ("Running Main Program")
        #import Main
        os.system("python Bin/Main.py")
    elif Result == "3":
        print ("Exit Program")
        quit()
    else:
        print (Result)


