class Laptop:
	def __init__(self,brand,name,price):
		self.brand=brand
		self.name=name
		self.price=price
	def discount(self,dis):
		return ((100-dis)*self.price/100)


l1=Laptop("DELL","au",90191)
l2=Laptop("APPLE","ax",67882)

print(l1.brand)
print(l1.name)
print(l1.price)


dis=int(input("Enter the discount percentage"))

print("with discount : ")
print(Laptop.discount(l1,dis))

print(l2.brand)
print(l2.name)
print(l2.price)

print("With 10 percent discount")

print(l2.discount(10))



