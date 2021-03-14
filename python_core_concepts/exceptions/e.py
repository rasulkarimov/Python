print("welcome")

try:
  ch = input("enter you choise:")

  if int(ch) == 1:
      print("this is one")
  elif int(ch) == 2:
      print("this is 2")
  else:
      print("not found")

except SyntaxError:
    print("send mail to admin there is syntax issue ..")

except ValueError:
    print("ask you only put number")

except NameError:
    print("mail admin, there NameError")

except:
    print("mail admin")

finally:
  print("I'm logging out, good goodbye")
