#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import re
import sys
import select


# Constans Colors
WHITE = "\033[0m"
GRAY = "\033[0;37m"
MAGENTA = "\033[0;35m"
RED = "\033[1;31m"
GREEN_2 = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
CYANO = "\033[1;36m"
GREEN = '\033[92m'
RESET = "\e[0m"

# Regex 
EMAIL = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
"{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
"\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))
HOST = re.compile(r'((^|\s)[a-z0-9-.]*\.(\w{1,3})\b)')
MAC = re.compile(r'([0-9a-f]{2}(?::[0-9a-f]{2}){5})', re.IGNORECASE)
IP = re.compile(r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)([ (\[]?(\.|dot)[ )\]]?(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})")
ERROR = re.compile(r'(error|retry|failure|exception)', re.IGNORECASE)
SUCCESS = re.compile(r'(successfully|success)', re.IGNORECASE)
NUMBER = re.compile(r'(^\d*$)', re.IGNORECASE)
URL = re.compile(r'[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)')

def set_color(patron, color, texto):    
    setcolor = r'%s\1%s' %(color, WHITE)    
    texto_color = re.sub(patron, setcolor , texto)
    return texto_color

def check_stdin():
    return select.select([sys.stdin,],[],[],0.0)[0] != []

def apply_colors_with_general_regex(text):
    text = set_color(NUMBER, BLUE, text)
    text = set_color(MAC, YELLOW, text)
    text = set_color(EMAIL, GREEN, text)
    text = set_color(HOST, BLUE, text)
    text = set_color(ERROR, RED, text)
    text = set_color(SUCCESS, GREEN_2, text)
    text = set_color(IP, YELLOW, text)
    text = set_color(URL, CYANO, text)
    
    return text
    

def main():    
    parser = argparse.ArgumentParser( 
        description="""
        example 1: # tail -f log.txt | sw   
        example 2: # sw log.txt
""")
    parser.add_argument('file', nargs='?') 
    
    args = parser.parse_args()

    if check_stdin():
        print ("process pipeline")

        for line in sys.stdin:
            print( apply_colors_with_general_regex(line.replace("\n", "")) )   
       
        sys.exit(0)
    
    
    
    file_opended = open(args.file, "r")
    file_readed = file_opended.read()
    file_opended.close()

    print (apply_colors_with_general_regex (file_readed))         

    sys.exit(0)


if __name__ == '__main__':
    main()







