class Cbox:
    "Class to hold ciphertext and implement helper functions"
    def __init__(self, keylength, cryptofile=None, cryptotext=None):

        self._keylength = int(keylength)
        
        if cryptofile is not None:
            cfile = open(cryptofile)
            self._ctext = cfile.read()
        if cryptotext is not None:
            self._ctext = cryptotext

    @property
    def keylength(self):
        return self._keylength

    @property
    def ctext(self):
        return self._ctext
            
