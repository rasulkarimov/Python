class visitor:
    #class variable : global scope
    country = "IN"
    num_of_visitor = 0
    
    def __init__(self, n, l, p):
        
        # instance variable
        self.name = n
        self.lname = l
        self.phone = p
        self.role = "visitor"
        
        visitor.num_of_visitor += 1
        
    def ret_phone(self):
        return self.phone
    
    def ret_full_name(self):
        return self.name + " " + self.lname
    
    def ret_my_role(self):
        return "my role is: " + self.role

class emp(visitor):
    # childclass, here we can change method / function
    def ret_my_role(self):
        self.role = "emplo"
        return "my role is: " + self.role
    pass

class student(visitor):
        # childclass, here we can change method / function
    def set_course(self):
        self.course = "python"
        return self.course

rasul = emp("rasul", "karimvov", 9876)

rasul.ret_my_role()

rasul.ret_full_name()

tom = student("tom", "ltom", 6543)

tom.set_course()

rasul.__dict__
