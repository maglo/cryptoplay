"""Vigenere Cipher Solver

Usage:
   vigenere.py crack <ciphertext> --keylength=<int>
   vigenere.py analyze <ciphertext> [--max-key-length=<int>]
   vigenere.py (-h | --help)

Options:
   -h --help         Show this screen
   --version         Show version


"""

from docopt import docopt

if __name__ == '__main__':
    clargs = docopt(__doc__, version="Vigenere Cipher Solver 0.1")
    print(clargs)
                    
