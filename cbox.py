class Cbox:
    """Class to hold ciphertext and implement helper functions"""

    def __init__(self, keylength, ciphertext):
        self.MAX_KEYLENGTH = 16
        self.set_keylength(keylength)

        if ciphertext is not None:
            self.set_ctext(ciphertext)
            if not self.sanity_check():
                raise ValueError("invalid ciphertext or keylength")
        
    def get_keylength(self):
        return self._keylength
    
    def set_keylength(self,value):
        self._keylength = int(value)
        key = []
        for i in range(0, int(value)):
            key.append(0)
        self.set_key(key)

    def get_ctext(self):
        return self._ctext

    def set_ctext(self, value):
        self._ctext = value

    def get_clist(self):
        retval = []
        numbytes = 2
        ctext = self.get_ctext()
        for i in range(0,len(ctext),numbytes):
            retval.append(int(ctext[i:i+numbytes], 16))
        return retval

    def get_bisection(self):
        retval = []
        clist = self.get_clist()
        keylength = self.get_keylength()
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
    
    def get_key(self):
        return self._key
    
    def set_key(self, value):
        if len(value) == self.get_keylength():
            self._key = value
        else:
            raise ValueError("invalid keylength")

    def decrypt(self):
        clist = self.get_clist()
        numitems = len(clist)
        keylength = self.get_keylength()
        key = self.get_key()
        retval = []
        
        for cursor in range(0, numitems):
            cbyte = clist[cursor]
            keycursor = cursor % keylength 
            pbyte = cbyte ^ key[keycursor]
            retval.append(pbyte)

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
