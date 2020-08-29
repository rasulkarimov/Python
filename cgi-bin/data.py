#!/usr/bin/python3
print("content-type: text/html")
print()

import subprocess
x=subprocess.getoutput("date")
print(x)
