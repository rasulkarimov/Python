#!/usr/bin/python3
import webbrowser
print("welcome")


print("Enter you requirements: " , end='')
ch=input()

if "date" in ch:
  webbrowser.open("http://192.168.0.71/cgi-bin/iiec.py?x=date")

elif "calendar" in ch:
  webbrowser.open("http://192.168.0.71/cgi-bin/iiec.py?x=cal")

else:
  print("not understood") 
