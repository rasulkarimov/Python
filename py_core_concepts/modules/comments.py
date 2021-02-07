def db(name, city, country="Russia"):
    """
    -------------------------------------------------
    This is finction for db
    required arguments:
    name: <name>           // mandatory argument
    city: <cityname>       // mandatory argument
    country=<countryname>  // optional, default value is Russia
    -------------------------------------------------
    """
    return "Name: " + name + ", City: " + city + ", Country: " + country

print(db.__doc__)  #  print doc information that was set above

print(db(name="Rasul",city="Moscow"))
