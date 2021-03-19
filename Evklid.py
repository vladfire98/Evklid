def Evklid(a,b):
	while b>0:
		c = a%b
		a = b
		b = c
	print(a)

def Evklid_long(a,b):
	while a != b:
		if a > b:
			a = a - b
		else:
			b = b - a
	print(a)
