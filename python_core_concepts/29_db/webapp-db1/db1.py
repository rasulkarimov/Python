from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("iiecapp")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb/data.sqlite'

# ORM (Object Releation Mapper)
db = SQLAlchemy(app)
print(db)

class IIEC(db.Model):
  id = db.Column( db.Integer, primary_key = True)
  name = db.Column( db.Text )
  age = db.Column( db.Integer )
  remarks = db.Column( db.Text )

  def __init__(self, name, age, remarks):
      self.name = name
      self.age = age
      self.remarks = remarks

db.create_all()

# Create

tom = IIEC("tom", 35, "good")
db.session.add(tom)
db.session.commit()


# Read
'''
r2 = IIEC.query.get(2)
print(r2.name, r2.age, r2.remarks)

r_all = IIEC.query.all()
print(r_all[0].name, r_all[0].age, r_all[0].remarks)

r_age = IIEC.query.filter_by(remarks='ok')
print(r_age.all())

# Update 
r1 = IIEC.query.get(1)
r1.age = 15
db.session.add(r1)
db.session.commit()
'''

# Delete
'''
r_all_rec = IIEC.query.get(2)
db.session.delete(r_all_rec)
db.session.commit()
'''
