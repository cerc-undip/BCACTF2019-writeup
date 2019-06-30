#!/usr/bin/python3

one = open("one.txt", "r")
two = open("two.txt", "r")

one_hex = one.read().split(" ")
two_hex = two.read().split(" ")

result = []
for i in range(len(one_hex)):
  temp = int(one_hex[i], 16) + int(two_hex[i], 16)
  result.append(temp)

result = [chr(x) for x in result]

print("".join(map(str, result)))
