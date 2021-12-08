#!/usr/bin/python3

import dis
magic = __import__('103-magic_class').MagicClass

pi = dis.dis(magic)
print(pi)
