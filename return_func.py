def outer_func():
	print("This is outer func")
	def inner_func(msg):
		print(msg)
	return inner_func



func1=outer_func()# address of inner function is assigned to func1

func1("this is inner function")