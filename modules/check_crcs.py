#!/usr/bin/env python3
"""Bandingkan CRC di vmlinux.symvers dengan CRC yang diminta modul vendor ROM."""
import sys
symvers, required = sys.argv[1], sys.argv[2]
have = {}
for line in open(symvers):
    f = line.rstrip("\n").split("\t")
    if len(f) >= 2:
        have[f[1]] = int(f[0], 16)
bad = checked = 0
for line in open(required):
    if line.startswith("#"):
        continue
    crc, sym, mods = line.rstrip("\n").split("\t")
    if sym not in have:  # simbol dari modul lain, bukan dari vmlinux
        continue
    checked += 1
    if have[sym] != int(crc, 16):
        bad += 1
        print(f"MISMATCH {sym}: kernel 0x{have[sym]:08x} != modul {crc} ({mods})")
print(f"{checked} simbol vmlinux dicek, {bad} tidak cocok")
sys.exit(1 if bad else 0)
