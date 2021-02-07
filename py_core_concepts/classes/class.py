class visitor:
    # attribute: variable
    # class var
    title = "Ericsson visitor"
    name = ""
    phone = ""
    
    # cunstructor : function : method
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        print("this is visitor class ... testing")
    
    # method: function
    def get_name(self):
        print("name is : " , self.name)
        
    def send_sms(self):
        print("send sms to: ", self.phone)
        #print(x)


# instantiation
# jack: object - instance
jack = visitor("Jack", 12345)

jack.name

jack.send_sms()



