a = input("Nhập số a:")
b = input("Nhập số b:")

def swap(a,b):
	tam = a
	a = b
	b = tam
	print('số a sau khi swap:',a)
	print('số b sau khi swap:',b)

swap(a,b)
