class person:
    def __init__(self,fname,lname,age):
        #instance variable
        print("constructor ,method is called")
        self.first_name=fname
        self.last_name=lname
        self.age=age
        self.full_name=fname+' '+lname
p1=person("sahil","mund",20)
p2=person("sammy","daniel",21)
print(p1.first_name)
print(p2.last_name)
print(p1.full_name)

