class Cbox:
    "Class to hold ciphertext and implement helper functions"
    def __init__(self, keylength, cryptofile=None, cryptotext=None):

        self._keylength = int(keylength)
        
        if cryptofile is not None:
            cfile = open(cryptofile)
            ctext = cfile.read()
            if self.sanity_check(ctext):
                self._ctext = ctext
            else:
                raise ValueError("invalid ciphertext")
        if cryptotext is not None:
            if self.sanity_check(cryptotext):
                self._ctext = cryptotext
            else:
                raise ValueError("invalid ciphertext")

    @property
    def keylength(self):
        return self._keylength

    @property
    def ctext(self):
        return self._ctext
            
    def sanity_check(self, ctext):
        #check length of ctext - should be even number and > 0
        length = len(ctext)

        if length > 0:
            retval = True
        else:
            retval = False
            
        if (length % 2) == 0:
            retval = retval & True
        else:
            retval =  retval & False

        return retval
