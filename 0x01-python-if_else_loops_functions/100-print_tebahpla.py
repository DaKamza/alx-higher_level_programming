#!/usr/bin/python3
# 100-print_tebahpla.py

i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print(chr(c - (32 if (c - ord('a')) % 2 == 0 else 0)), end="")
