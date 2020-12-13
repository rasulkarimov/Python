#!/usr/bin/python3

import sys

fl = str(sys.argv[1])

try:
  fh = open(fl, mode='r')
except FileNotFoundError:
  print("File {} not found".format(fl))
  exit(1)
print(fh.read())
fh.close()
