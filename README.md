cryptoplay
==========

Attempts to break a Vigenere Cipher variant.

Vigenere Cipher Variant
-----------------------
The plaintext message *m* is encrypted by XOR-ing each byte in *m* using a byte from an *N*-byte key *k*, producing a ciphertext *c*.
If *N* < |*m*|, *k* is repeated.

<P>c<sub>i</sub> = m<sub>i</sub> ⊕ k<sub>[i mod N]</sub></P>

The program expects the ciphertext to be encoded with hexadecimal two-byte representations for each byte in *c*.

So if *c* is `0xDE 0xAD 0xBE 0xEF` it should be endoced as `DEADBEEF`.

Cracking the Vigenere Cipher
----------------------------
Read more about the Vigenere Cipher at [Wikipedia](http://en.wikipedia.org/wiki/Vigenère_cipher)

To brute force the variant would take 256 ^ N time.

But using statistical analysis it is possible to reduce the time to crack the ciphertext to N * 256.

First, the keylength is determined, then each byte of the message is brute forced.

Running the Program
-------------------
To run the program:

	python vigenere.py crack -f challenge --keylength 7

The keylength brute forcer is not implemented yet. 
The keylength could be determined by [vigenereSolveR](https://github.com/maglo/vigenereSolveR/blob/master/determineKeyLength.R).

