"""Vigenere Cipher Solver

Usage:
   vigenere.py crack (<ciphertext> | -f <cipherfile>) --keylength=<int>  [--verbose]
   vigenere.py analyze (<ciphertext> | -f <cipherfile>) [--max-keylength=<int>] [--verbose]
   vigenere.py encrypt (<plaintext> | -f <plainfile>) (--key <key> | <keyfile>) [--verbose]
   vigenere.py decrypt (<ciphertext> | -f <cipherfile>) (--key <key> | <keyfile>) [--verbose]
   vigenere.py (-h | --help)

Options:
   -h --help         Show this screen
   --version         Show version
   --verbose         Debug output

"""

from docopt import docopt
from sys import exit
import brute
import logging

VERSION = "0.1"

if __name__ == '__main__':
    clargs = docopt(__doc__, version=VERSION)

    if clargs["--verbose"]:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO
        
    logging.basicConfig(filename='output.log', level=loglevel, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.info('=' * 8 + 'Start' + '=' * 8)
        

    if clargs['analyze']:
        print("Not implemented yet. Bummer")
        logging.info('=' * 8 + 'Stop' + '=' * 8)
        exit(0)

    if clargs['encrypt']:
        print("Not implemented yet. Bummer")
        logging.info('=' * 8 + 'Stop' + '=' * 8)
        exit(0)

    if clargs['decrypt']:
        print("Not implemented yet. Bummer")
        logging.info('=' * 8 + 'Stop' + '=' * 8)
        exit(0)

    if clargs['crack']:
        keylength = clargs["--keylength"]
        if clargs['-f']:
            cipherfile = clargs["<cipherfile>"]
            cfile = open(cipherfile)
            ciphertext = cfile.read()
        else:
            ciphertext = clargs["<ciphertext>"]

        brute = brute.Brute(ciphertext = ciphertext, keylength = keylength)
        ptext = brute.get_ptext()
        
        print(ptext)

        logging.info('=' * 8 + 'Stop' + '=' * 8)
        exit(0)
                    
