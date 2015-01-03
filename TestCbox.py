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

    def test_text_invalid(self):
        keylength = 7
        ctext = "AABBCCDDEEF"
        with self.assertRaises(ValueError):
            _cbox = cbox.Cbox(keylength, cryptotext=ctext)


        
if __name__ == '__main__':
    unittest.main()
