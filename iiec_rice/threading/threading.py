import threading

def a():
    while True:
      print("a")
def b():
    while True:
      print("b")
x1 = threading.Thread( target=a )
x2 = threading.Thread( target=b )

x1.start()
x2.start()

