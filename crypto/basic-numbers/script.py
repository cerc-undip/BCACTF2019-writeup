#!/usr/bin/python3

raw = open("quest.txt", "r").read()

binary = raw.split(" ")
binary = [chr(int(x, 2)) for x in binary]

print(''.join(map(str, binary)))
