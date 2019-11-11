list=[]
class Customer:
    def __int__(self):
        self.name=''
        self.password=''
        self.email=''
        self.mobile=''

    def addCustomer(self):
        list.append(self)
while(True):
    c = Customer()
    c.name=input("Enter name")
    c.password=input("Enter password")
    c.email=input("Enter email")
    c.mobile=input("Enter mobile number")

    c.addCustomer()
    print("Customer added successfully")
    ch=int(input("Enter choice="))
    if(ch==0):
        break
for v in list:
    print(v.name,v.password,v.email,v.mobile)


