import os
os.chdir('/Users/chellshelove/Documents/GitHub/book')
myBook = open("66689-0.txt", "r")

import re

def hapax(file):
    file = open(file)
    words = re.findall('\w+', file.read().lower())
    freqs = {key: 0 for key in words}
    for myBook in words:
        freqs[myBook] += 1
    for myBook in freqs:
        if freqs[myBook] == 1:
            print(myBook)
            
hapax('66689-0.txt')