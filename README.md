LOCKET
======

An AES encryption script written in Python. Can encrypt and decrypt many files at once.

A work in progress. Do not use.

## INSTALLATION

Straight from the Git repository:

    $ git clone 
    $ pip install -r requirements
    $ python setup.py  

Using PIP:

    $ pip install locket

## USAGE

For a full listing of available commands, use `locket --help`. Basic usage is as follows:

To encrypt a file and save it in the current working directory (as `file.txt.enc`):

    $ locket -e file.txt

To decrypt the file 

    $ locket -d file.txt.enc

This will decrypt an encrypted file, assuming the password (or key) that you provide is correct.
 

## DISCLAIMER

Use with discretion. Files are encoded with the password that you provide, and there is no way to re

## TODO

- Encrypt/Decrypt large files in chunks