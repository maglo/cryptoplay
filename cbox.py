class Cbox:
    "Class to hold ciphertext and implement helper functions"

    def __init__(self, keylength, cryptofile=None, cryptotext=None):
        self.MAX_KEYLENGTH = 16
        self._keylength = int(keylength)

        if cryptotext is not None:
            self._ctext = cryptotext
            if not self.sanity_check():
                raise ValueError("invalid ciphertext or keylength")
        
        if cryptofile is not None:
            cfile = open(cryptofile)
            self._ctext = cfile.read()
            if not self.sanity_check():
                raise ValueError("invalid ciphertext or keylength")


    @property
    def keylength(self):
        return self._keylength

    @property
    def ctext(self):
        return self._ctext

    @property
    def clist(self):
        retval = []
        numbytes = 2
        for i in range(0,len(self.ctext),numbytes):
            retval.append(int(self.ctext[i:i+numbytes], 16))
        return retval

    @property
    def bisection(self):
        retval = []
        clist = self.clist
        keylength = self._keylength
        items = len(clist) // keylength
        remain = len(clist) % keylength
        
        for keyindex in range(0, keylength):
            sublist = []
            
            for cursor in range(0, items):
                item = clist[keyindex + cursor * keylength]
                sublist.append(item)

            if remain > keyindex:
                item = clist[keyindex + (cursor + 1) * keylength]
                sublist.append(item)

            retval.append(sublist)
                
        return retval
    
    def sanity_check(self):
        #check length of ctext - should be even number and > 0
        length = len(self._ctext)

        if length > 0:
            retval = True
        else:
            retval = False
            
        if (length % 2) == 0:
            retval = retval & True
        else:
            retval =  retval & False

        # check that ctext only contains 0 - 9, A - F
        whitelist = "ABCDEF0123456789"
        if all(c in whitelist for c in self._ctext):
            retval = retval & True
        else:
            retval = retval & False
            
        # check keylength
        if self._keylength > 0 and self._keylength < self.MAX_KEYLENGTH:
            retval = retval & True
        else:
            retval = retval & False
            
        return retval
