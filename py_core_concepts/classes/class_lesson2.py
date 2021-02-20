class visitor:
    #class variable : global scope
    country = "IN"
    
    def __init__(self, n, l, p):
        
        # instance variable
        self.name = l
        self.lname = p
        self.phone = n
    def ret_phone(self):
        return self.phone


jack = visitor("jack", "xyz", 12345)


jack.__dict__

jack.name = 12345

jack.ret_phone()

jack
