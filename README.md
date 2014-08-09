LOCKET
======

An AES encryption script written in Python. Can encrypt and decrypt many files at once.

## INSTALLATION

Straigt from the Git repository:

    $ git clone 
    $ pip install -r requirements
    $ python setup.py  

Using PIP:

    $ pip install locket

## USAGE

    $ locket -e file.txt
    
The above command will encrypt file.txt and save it in the current working directory.

    $ locket -d file.txt.dat

This will decrypt an encrypted file, assuming the password (or key) that you provide is correct.
 

## DISCLAIMER

Use with discretion. Files are encoded with the password that you provide, and there is no way to re