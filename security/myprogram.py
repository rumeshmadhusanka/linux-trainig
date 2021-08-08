#!/usr/bin/env python3
import hashlib #imported as asked in the question
from sys import argv # required to parse commmand line argumanets 
#Command line args look like this: python3 myprogam.py hello
#First argument to the command python3 is 'myprogam.py'-the file name ---> index 0
#Second argument is hello --> index 1

salt = bytearray("Km5d5ivMy8iexuHcZrsD", "utf8")
hash_algo = "SHA512"
iterations = 200000
try:
    assert len(argv) > 1 #checking if the argumet is passed
    value = bytearray(argv[1], "utf8") #argv is an array 
    # password and salt both has to be given as bytes, not strings
    hash_value = hashlib.pbkdf2_hmac(hash_name=hash_algo, password=value, iterations=iterations, salt=salt)
    print(hash_value.hex()) # convert to readable format using hex() and disply on command line
except AssertionError:
    print("Incorrect number of arguments")
except Exception:
    print("Exception occurred")
