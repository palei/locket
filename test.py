from locket import AESCipher
import unittest

class AESCipherTest(unittest.TestCase):
    
    def setUp(self):
        self.cipher = AESCipher()
        self.cipher.set_key('testkey')

    def test_encrypt_and_decrypt(self):
        text = 'This is some random text.'

        data = self.cipher.encrypt(text)

        self.assertEquals(text, self.cipher.decrypt(data), 'The decrypted data should be equal to the text.')

if __name__ == '__main__':
    unittest.main()
