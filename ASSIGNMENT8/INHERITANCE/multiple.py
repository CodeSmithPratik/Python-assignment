class Fname:
    Fname = ""
 
    def Fname(self):
        print(self.Fname)
 
 
 
class Lname:
    Lname = ""
 
    def Lname(self):
        print(self.Lname)
 
 
class student(Fname, Lname):
    def parents(self):
        print("First Name :", self.Fname)
        print("Last Name :", self.Lname)
 
s1 = student()
s1.Lname = "Nikam"
s1.Fname = "Adarsh"
s1.parents()