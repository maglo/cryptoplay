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

    def test_file_invalid(self):
        testfile = "test_invalid"
        keylength = 7
        cfile = open(testfile)
        ctext = cfile.read()

        with self.assertRaises(ValueError):
            _cbox = cbox.Cbox(keylength, cryptofile=testfile)


    def test_text(self):
        keylength = 7
        ctext = "AABBCCDDEEFF"
        
        _cbox = cbox.Cbox(keylength, cryptotext=ctext)
        self.assertEqual(keylength, _cbox.keylength)
        self.assertEqual(ctext, _cbox.ctext)

    def test_text_invalid_keylength_1(self):
        keylength = -1
        ctext = "AABBCCDDEEFF"

        with self.assertRaises(ValueError):
            _cbox = cbox.Cbox(keylength, cryptotext=ctext)

    def test_text_invalid_keylength_2(self):
        keylength = 100
        ctext = "AABBCCDDEEFF"
        
        with self.assertRaises(ValueError):
            _cbox = cbox.Cbox(keylength, cryptotext=ctext)


    def test_text_invalid(self):
        keylength = 7
        ctext = "AABBCCDDEEF"
        with self.assertRaises(ValueError):
            _cbox = cbox.Cbox(keylength, cryptotext=ctext)

    def test_text_invalid_1(self):
        keylength = 7
        ctext = "AABBCCDDEEFG"
        with self.assertRaises(ValueError):
            _cbox = cbox.Cbox(keylength, cryptotext=ctext)

    def test_clist(self):
        keylength = 7
        ctext = "AABBCCDDEEFF"
        clist = [0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]
        
        _cbox = cbox.Cbox(keylength, cryptotext=ctext)
        self.assertEqual(keylength, _cbox.keylength)
        self.assertEqual(clist, _cbox.clist)
        
    def test_bisection(self):
        keylength = 3
        ctext = "1112132122233132334142"
        clists = [
            [0x11, 0x21, 0x31, 0x41],[0x12, 0x22, 0x32, 0x42],[0x13, 0x23, 0x33]
        ]

        _cbox = cbox.Cbox(keylength, cryptotext=ctext)
        self.assertEqual(keylength, _cbox.keylength)
        self.assertEqual(clists, _cbox.bisection)

if __name__ == '__main__':
    unittest.main()
