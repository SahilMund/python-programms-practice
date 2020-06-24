#instance methods
class person:
    def __init__(self,fname,lname,age):
        #instance variable
        print("constructor ,method is called")
        self.first_name=fname
        self.last_name=lname
        self.age=age

    def full_name(self,x):
        return f"{self.first_name} {x} {self.last_name}"
p1=person("sahil","mund",20)
p2=person("sammy","daniel",21)
print(p1.full_name("ranjan"))
