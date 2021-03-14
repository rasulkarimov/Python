class visitor:
    
    region = "RU"
    
    # statick method
    @staticmethod # annotation / decorator
    def ctime():
        return "today is monday"
    
    # class method
    @classmethod  # annotation / decorator
    def get_region(cls):
        return cls.region
    @classmethod
    def set_region(cls, newregion):
        cls.region = newregion
        return cls.region
    
    def __init__(self, first, last, mob):
        self.firstname = first
        self.lastname = last
        self.mobile= mob
        
    # instance method : getter
    def get_fullname(self):
        return self.firstname + " " + self.lastname
    # instance method : setter
    def set_mobile(self, newmob):
        self.mobile = newmob

class emp(visitor):
    def __init__(self, first, last, mob, title):
        super().__init__(first, last, mob)
        self.jobtitle = title
    def set_title(self, title):
        self.jobtitle = title

# help(emp)
jack = emp(first="jack", last="ljack", mob=1234, title='manager')

jack.get_fullname()

visitor.get_region()

visitor.set_region('US')

jack.get_region()

jack.ctime()
