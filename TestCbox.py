import unittest
import cbox

class TestCbox(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_text(self):
        keylength = 7
        ctext = "AABBCCDDEEFF"
        
        _cbox = cbox.Cbox(keylength, ciphertext=ctext)
        self.assertEqual(keylength, _cbox.get_keylength())
        self.assertEqual(ctext, _cbox.get_ctext())

    def test_text_invalid_keylength_1(self):
        keylength = "-1"
        ctext = "AABBCCDDEEFF"

        with self.assertRaises(ValueError):
            _cbox = cbox.Cbox(keylength, ciphertext=ctext)

    def test_text_invalid_keylength_2(self):
        keylength = "100"
        ctext = "AABBCCDDEEFF"
        
        with self.assertRaises(ValueError):
            _cbox = cbox.Cbox(keylength, ciphertext=ctext)


    def test_text_invalid(self):
        keylength = "7"
        ctext = "AABBCCDDEEF"
        with self.assertRaises(ValueError):
            _cbox = cbox.Cbox(keylength, ciphertext=ctext)

    def test_text_invalid_1(self):
        keylength = "7"
        ctext = "AABBCCDDEEFG"
        with self.assertRaises(ValueError):
            _cbox = cbox.Cbox(keylength, ciphertext=ctext)

    def test_clist(self):
        keylength = "7"
        ctext = "AABBCCDDEEFF"
        clist = [0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]
        
        _cbox = cbox.Cbox(keylength, ciphertext=ctext)
        self.assertEqual(int(keylength), _cbox.get_keylength())
        self.assertEqual(clist, _cbox.get_clist())
        
    def test_cipherstreams_vigenere(self):
        keylength = "3"
        ctext = "1112132122233132334142"
        clists = [
            [0x11, 0x21, 0x31, 0x41],[0x12, 0x22, 0x32, 0x42],[0x13, 0x23, 0x33]
        ]

        _cbox = cbox.Cbox(keylength, ciphertext=ctext)
        self.assertEqual(int(keylength), _cbox.get_keylength())
        self.assertEqual(clists, _cbox.get_cipherstreams_vigenere())

    def test_decryption(self):
        keylength = "3"
        key = [ 0x01, 0x02, 0x03 ]
        ptext = [ 0xDE, 0xAD, 0xBE, 0xEF ]
        ctext = "DFAFBDEE"
        _cbox = cbox.Cbox(keylength, ciphertext=ctext)
        _cbox.set_key(key)
        dec = _cbox.decrypt()
        self.assertEqual(ptext, dec)

    def test_keylength(self):
        keylength = "3"
        ctext = "DFAFBDEE"
        _cbox = cbox.Cbox(keylength, ciphertext=ctext)
        self.assertEqual(int(keylength), _cbox.get_keylength())

        keylength = "4"
        _cbox.set_keylength(keylength)
        retval = _cbox.get_keylength()
        key = _cbox.get_key()
        self.assertEqual(retval, int(keylength))
        self.assertEqual([0x00, 0x00, 0x00, 0x00], key)

    def test_key_property(self):
        keylength = "3"
        key = [ 0x01, 0x02, 0x03 ]
        ctext = "DFAFBDEE"
        _cbox = cbox.Cbox(keylength, ciphertext=ctext)

        retkey = _cbox.get_key()
        self.assertEqual([0x00, 0x00, 0x00], retkey)

        _cbox.set_key(key)
        retkey = _cbox.get_key()
        self.assertEqual(key,retkey)

        key = [ 0x01, 0x02, 0x03, 0x04 ]
        with self.assertRaises(ValueError):
            _cbox.set_key(key)


if __name__ == '__main__':
    unittest.main()
