#!/usr/bin/env python

import os
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        salt = os.urandom(8) # 64 bits.

    assert 8 == len(salt)
    assert isinstance(salt, str)

    if isinstance(password, unicode):
        password = password.encode('UTF-8')

    assert isinstance(password, str)

    result = password
    for i in xrange(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result

def validate_password(hashed, input_password):
    return hashed == encrypt_password(input_password, salt=hashed[:8])

def file_read(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    return lines

def file_write(filename,passwd_list):
    with open(filename,'aw') as f:
        for passwd in passwd_list:
            f.write(passwd + '\n')

if __name__  == '__main__':
    input_filename = 'original_passwd.txt'
    output_filename = 'hashed_passwd.txt'
    passwd_list = [ encrypt_password(passwd) for passwd in file_read(input_filename) ]
    file_write(output_filename,passwd_list)