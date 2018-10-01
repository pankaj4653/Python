class csstudent:
	stream=0
	def __init__(self,name,roll,age):
		csstudent.stream=csstudent.stream+1
		self.name=name
		self.roll=roll
		self.age=age
	def display(self):
		print(self.stream)
		print(self.name)
		print(self.roll)
		print(self.age)


c1=csstudent("Shubham",34,20)

c1.display()
c2=csstudent("Payal",29,89)
c3=csstudent("Gaurav",23,90)

c3.stream=9
print(c3.__dict__)
print(c1.__dict__)
print(c3.stream)
print(c1.stream)


print(f"Number of students {c3.stream} ")


