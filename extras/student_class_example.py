class student:
     def __init__(self,name):
          self.name=name
          self.attendence=0
          self.marks=[]
          print("Welcome {} to the school".format(name))
     def addmarks(self,m):
          self.marks.append(m)
     def attend_days(self):
          self.attend +=1
     def getavg(self):
          return sum(self.marks)/len(self.marks)
