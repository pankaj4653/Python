class Person:
	def __init__(self,fname,lname,age):
		self.fname=fname
		self.lname=lname
		self.age=age

	def fullname(self):
		return f"{self.fname}  {self.lname}"

	def is_above_18(self):
		return self.age>18


p1=Person("Abhilash","Jha",23)
p2=Person("Saif","Ali",15)


print(p1.fullname())
print(Person.fullname(p2)) #this is the alternative way to call the function

print(p1.is_above_18())
print(p2.is_above_18())
