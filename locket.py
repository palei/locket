#!/usr/bin/env python
import Crypto.Cipher.AES as AES
import Crypto.Random as Random
import optparse
import base64
import sys, os

class AESCipher(object):

    def __init__(self, key=None):
        self.bs = 32
        if key: 
            self.set_key(key)

    def set_key(self, key):
        if len(key) > self.bs: 
            self.key = self.key[:self.bs]
        else: 
            self.key = self.pad(key)

    def pad(self, s):
        return s + (self.bs - len(s) % self.bs)*chr(self.bs - len(s) % self.bs)

    def unpad(self, s):
        return s[:-ord(s[len(s)-1:])]

    def encrypt(self, data):
        data = self.pad(data)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(data))

    def decrypt(self, data):
        data = base64.b64decode(data)
        iv = data[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self.unpad(cipher.decrypt(data[16:]))

parser = optparse.OptionParser()


parser.add_option('-e', '--encrypt', action='store_true', dest='encrypt')
parser.add_option('-d', '--decrypt', action='store_true', dest='decrypt')
parser.add_option('-p', '--password', dest='password')
parser.add_option('-s', '--save', action='store_true', dest='save')

def read_file(filename):
    with open(filename, 'r') as fh:
        return fh.read()

def save_file(data, filename, suffix=None):
    with open(filename + suffix, 'w') as fh:
        fh.write(data)

def read_file_in_chunks(filename, chunk_size=1024):
    pass

def main():

    cipher = AESCipher()

    (options, args) = parser.parse_args()

    if options.encrypt and options.decrypt:
        sys.exit("cant handle -e and -d togehter, aborting")

    if not options.password:
        options.password = raw_input('password: ')

    cipher.set_key(options.password)

    for filename in args:
        if not os.path.exists(filename):
            continue

        data = read_file(filename)
        
        if options.encrypt: 
            data = cipher.encrypt(data)

        if options.decrypt:
            data = cipher.decrypt(data)

        if options.save:
            save_file(data, filename, suffix='.AES')
        else:
            print data

if __name__ == '__main__':
    main()