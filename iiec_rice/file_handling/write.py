#!/usr/bin/python3

import sys

fl = str(sys.argv[1])

try:
  fh = open(fl, mode='r+')
  print("Current content:\n"+fh.read())
except FileNotFoundError:
  fh = open(fl, mode='w+')

newline = input("Enter content to append:\n")
fh.write(newline+"\n")
fh.seek(0, 0)

print("\nNew content is:")
print(fh.read())

fh.close()
