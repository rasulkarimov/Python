#wsgi.py file creates an application object (or callable) so that the server can use it
from app import application
if __name__ == "__main__":
  application.run()
