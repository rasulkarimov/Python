#!/usr/bin/python3

import subprocess
import os
import getpass

inpass = getpass.getpass("enter you pass: ")
apass = "lw"

if inpass != apass:
  print("you pass wrong")
  exit()

x = subprocess.getstatusoutput("date")
print(x)

status = x[0]
output = x[1]
