class Person:
	
	rate=10
	def __init__(self,fname,lname,age,pay):
		self.name=fname
		self.lname=lname
		self.age=age
		self.pay=pay
		self.fullname=fname+" "+lname

	def details(self):
		print("The details of the Employee : ")
		print(f"Name :  {self.fullname}")
		print(f"Age : {self.age}")
		print(f"Pay : {self.pay}")
		print(f"Rate : {self.rate}")

	@classmethod
	def string_func(cls,emp):
		fname, lname, age, pay =emp.split('-')
		return cls(fname,lname,int(age),int(pay))

	




p1=Person("Ram","Roshan",22,908823)

emp1="Raj-Kumar-32-1010101"
p2=Person.string_func(emp1)


p2.details()
p1.details()


# print(p1.__dict__)

# p1.details()


