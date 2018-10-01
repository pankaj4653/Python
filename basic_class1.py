
class Person:
	def __init__(self,first_name,last_name,age):
		self.first_name=first_name
		self.last_name=last_name
		self.age=age


p1=Person("Avinash","Kumar",24)
p2=Person("Abhishek","Kumar",24)

print(p1.first_name+" "+p1.last_name)
print(p2.first_name+" "+p2.last_name)
