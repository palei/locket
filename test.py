from locket import AESCipher, save_file, read_file
import unittest, os

class LocketTest(unittest.TestCase):
    
    def setUp(self):
        self.cipher = AESCipher()
        self.cipher.set_key('testkey')

    def test_encrypt_and_decrypt(self):
        text = 'This is some random text.'
        data = self.cipher.encrypt(text)

        assert self.cipher.decrypt(data) == text, 'Decrypted data is not equal to text'

    def test_one_is_not_two(self):
        assert 1 != 2, 'One should not equal two'

    def test_save_file(self):
        filename, text = 'test.txt', 'This message will self-destruct in 3 seconds.'
        data = self.cipher.encrypt(text)
        save_file(data, filename)

        assert os.path.exists('test.txt') == True, 'Saved file should exist.'

        data = read_file(filename)

        assert self.cipher.decrypt(data) == text, 'Data read and encrypted from file should equal text'


if __name__ == '__main__':
    unittest.main()
