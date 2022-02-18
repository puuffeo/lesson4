n = int(input("число:"))
a = 0 
b = 0
while n >0:
	if  n % 2 ==0:
		n //= 10 
	else: 
		s = n % 10
		print(s) 
		n //= 10 
