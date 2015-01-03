"""Vigenere Cipher Solver

Usage:
   vigenere.py crack (<ciphertext> | -f <cipherfile>) --keylength=<int>
   vigenere.py analyze (<ciphertext> | -f <cipherfile>) [--max-keylength=<int>]
   vigenere.py (-h | --help)

Options:
   -h --help         Show this screen
   --version         Show version


"""

from docopt import docopt
from sys import exit
import cbox

VERSION = "0.1"

if __name__ == '__main__':
    clargs = docopt(__doc__, version=VERSION)
    
    if clargs['analyze']:
        print("Not implemented yet. Bummer")
        exit(0)

    if clargs['crack']:
        if clargs['-f']:
            #file open <cipherfile>
            #store contents in object and set keylength
            cbox = cbox.Cbox(cryptofile = clargs["<cipherfile>"], keylength=clargs["--keylength"])
            exit(0)
        else:
            #store contents of <ciphertext> in object and set keylength
            cbox = cbox.Cbox(cryptotext = clargs["<ciphertext>"], keylength=clargs["--keylength"])
            exit(0)
                    
