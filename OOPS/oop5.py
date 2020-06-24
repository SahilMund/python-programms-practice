#class methods
class person:
    count_instance=0
    def __init__(self,fname,lname,age):
        #instance variable
        person.count_instance += 1
        print("constructor ,method is called")
        self.first_name=fname
        self.last_name=lname
        self.age=age

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} of person classes"

    def full_name(self,x):
        return f"{self.first_name} {x} {self.last_name}"
p1=person("sahil","mund",20)
p2=person("sammy","daniel",21)
print(p1.full_name("ranjan"))
print(person.count_instances())
