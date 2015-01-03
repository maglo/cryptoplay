import unittest
import cbox

class TestCbox(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_file(self):
        testfile = "test"
        keylength = 7
        cfile = open(testfile)
        ctext = cfile.read()

        _cbox = cbox.Cbox(keylength, cryptofile=testfile)
        self.assertEqual(keylength, _cbox.keylength)
        self.assertEqual(ctext, _cbox.ctext)

    def test_text(self):
        keylength = 7
        ctext = "AABBCCDDEEFF"
        
        _cbox = cbox.Cbox(keylength, cryptotext=ctext)
        self.assertEqual(keylength, _cbox.keylength)
        self.assertEqual(ctext, _cbox.ctext)
        
if __name__ == '__main__':
    unittest.main()
