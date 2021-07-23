#!/usr/bin/env python3
import hashlib
from sys import argv
import secrets

try:
    assert len(argv) > 1
    salt = secrets.token_bytes(128)
    value = bytearray(argv[1], "utf8")
    hash_value = hashlib.sha512(salt+value)
    print(hash_value.hexdigest())
except AssertionError:
    print("Incorrect number of arguments")
except Exception:
    print("Exception occurred")
