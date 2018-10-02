def square(a):
	return a*a


print(square(7))
print(square)

print(square.__name__)# gives the actual name of the function

s=square# s and square points to the same location

print(s.__name__)

print(s)

print(s(9))

