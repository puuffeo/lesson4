a =int(input("трех значное число:"))
b = 0 
c = 0
while a > 0:
	c = a % 10 
	b = b+c
	a = a//10


print(b)
