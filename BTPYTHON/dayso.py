n = int(input("Nhập số n:"))

def inra(n):
	i = 1
	while i <= n:
		print(i)
		i+=1

def tongptchan(n):
	a = 0
	i = 1	
	while i <= n:
		if(i%2==0):
			a += i
		i += 1
	print('Tổng các số chẵn:'a)

inra(n)
tongptchan(n)
