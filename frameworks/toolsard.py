#ToolsARD by Joumsadd
from art import *
import time,os,sys
from colorama import Fore, init
init(strip=True)
init(autoreset=True, convert=True)

def gradual_art(art_text, font_style):
    text = text2art(art_text, font=font_style)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.007)  # Adjust the delay as needed
    print()  # Move to the next line after displaying the complete text

def art(text, fontStyle):
    text = text2art(text, font=fontStyle)
    print(text)

def fileWrite(fileName, type, content):
    with open(fileName, type) as file:
        file.write(content)

def fileRead(fileName):
    with open(fileName, 'r') as file:
        content = file.read()
        print(content)