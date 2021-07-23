#!/usr/bin/env python3
import hashlib
from sys import argv
import secrets

hash_algo = "SHA512"
iterations = 200000
try:
    assert len(argv) > 1
    salt = secrets.token_bytes(128)
    value = bytearray(argv[1], "utf8")
    hash_value = hashlib.pbkdf2_hmac(hash_name=hash_algo, password=value, iterations=iterations, salt=salt)
    print(hash_value.hex())
except AssertionError:
    print("Incorrect number of arguments")
except Exception:
    print("Exception occurred")
