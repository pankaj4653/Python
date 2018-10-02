



def func(a):
	return a*a

L=[1,2,3,4]

def map_func(func,L):
	l=[]
	for i in L:
		l.append(func(i*i))
	return l


def anfunc(func,map_func,L):
	return map_func(func,L)


print(anfunc(func,map_func,L))