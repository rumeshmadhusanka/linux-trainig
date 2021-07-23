#!/usr/bin/env python3
import hashlib
from sys import argv

salt = bytearray("Km5d5ivMy8iexuHcZrsD", "utf8")
hash_algo = "SHA512"
iterations = 200000
try:
    assert len(argv) > 1
    value = bytearray(argv[1], "utf8")
    hash_value = hashlib.pbkdf2_hmac(hash_name=hash_algo, password=value, iterations=iterations, salt=salt)
    print(hash_value.hex())
except AssertionError:
    print("Incorrect number of arguments")
except Exception:
    print("Exception occurred")
