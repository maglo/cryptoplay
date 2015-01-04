from __future__ import division
import cbox
import logging

log = logging.getLogger(__name__)

class Brute:
    """Class to brute force cipher streams"""

    def __init__(self, keylength, ciphertext):
        self.set_keylength(int(keylength))
        self.set_ciphertext(ciphertext)
        _cbox = cbox.Cbox(ciphertext = ciphertext, keylength=keylength)
        self.set_cbox(_cbox)
        self._ptext = ""
        self.create_english_freq_table()
        keybytes = self.brute()
        _cbox.set_key(keybytes)
        ptext_bytes = _cbox.decrypt()
        ptext = ""
        for pbyte in ptext_bytes:
            ptext += chr(pbyte)
        self.set_ptext(ptext)


    def get_keylength(self):
        return self._keylength

    def set_keylength(self, value):
        log.debug("Setting keylength %d" % value)
        self._keylength = value

    def get_ciphertext(self):
        return self._ciphertext

    def set_ciphertext(self, value):
        self._ciphertext = value
        
    def get_cbox(self):
        return self._cbox

    def set_cbox(self, value):
        if isinstance(value, cbox.Cbox):
            self._cbox = value
        else:
            log.error("Invalid object passed to set_cbox")
            raise ValueError("Only cboxes will do")

    def get_ptext(self):
        return self._ptext

    def set_ptext(self, value):
        self._ptext = value

    def brute(self):
        cbox = self.get_cbox()
        cipherstreams = cbox.get_cipherstreams_vigenere()
        number_of_streams = len(cipherstreams)
        log.debug("Received %d cipherstreams" % number_of_streams)

        keybytes = []

        for keypos in range(0, number_of_streams):
            log.debug("Analyzing keypos %d" % keypos)
            cstream = cipherstreams[keypos]
            best_key = 0
            best_score = 0
            for key in range(0, 0xff):
                pstream = []
                for cbyte in cstream:
                    pbyte = cbyte ^ key
                    pstream.append(pbyte)
                if self.is_printable(pstream):
                    score = self.calculate_score(pstream)
                    if score > best_score:
                        log.debug("Score: %f for key %d beats %d" % (score,key, best_key))
                        best_key = key
                        best_score = score
            keybytes.append(best_key)
            
        log.info("Candidate key: %s" % keybytes)
        return keybytes

    def is_printable(self, plainstream):
        #if all bytes in plainstream >= 32 <127 return true
        for pbyte in plainstream:
            if pbyte >= 0x20 and pbyte < 0x7f:
                pass
            else:
                return False

            return True
        
    def create_english_freq_table(self):
        freq = {}
        freq['a'] = 8.2
        freq['b'] = 1.5
        freq['c'] = 2.8
        freq['d'] = 4.3
        freq['e'] = 12.7
        freq['f'] = 2.2
        freq['g'] = 2.0
        freq['h'] = 6.1
        freq['i'] = 7.0
        freq['j'] = 0.2
        freq['k'] = 0.8
        freq['l'] = 4.0
        freq['m'] = 2.4
        freq['n'] = 6.7
        freq['o'] = 1.5
        freq['p'] = 1.9
        freq['q'] = 0.1
        freq['r'] = 6.0
        freq['s'] = 6.3
        freq['t'] = 9.1
        freq['u'] = 2.8
        freq['v'] = 1.0
        freq['w'] = 2.4
        freq['x'] = 0.2
        freq['y'] = 2.0
        freq['z'] = 0.1
        self._freq = freq
        
    def get_english_freq(self, char):
        freq = self._freq
        return freq[char]
    
    def calculate_score(self, plainstream):
        table = {}
        freq_table = {}
        numitems = len(plainstream)
        sum = 0
        
        for char in range(ord('a'), ord('z') + 1):
            table[chr(char)] = 0
            
        for pbyte in plainstream:
            if pbyte >=ord('a') and pbyte <= ord('z'):
                table[chr(pbyte)] += 1

        for char in range(ord('a'), ord('z')):
            q = table[chr(char)] / numitems
            p = self.get_english_freq(chr(char)) / 100
            sum += p * q

        return sum
