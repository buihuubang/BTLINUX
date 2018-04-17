a = int(input("Nhập số a:"))
b = int(input("Nhập sô b:"))

def cong(a,b):
	tong = a + b
	print('Tổng hai số là:',tong)

def tru(a,b):
	hieu = a - b
	print('Hiệu hai số là:',hieu)

def tich(a,b):
	tich = a * b
	print('Tích hai số là:',tich)

def thuong(a,b):
	thuong = a / b
	print('Thương hai số là:',thuong)

def luythua(a,b):
	luythua = 1
	for i in (0,b,1):
		luythua*=a
	print('Lũy thừa hai số là:',luythua)

def laydu(a,b):
	c = a % b
	print('Dư:', c )

cong(a,b)
tru(a,b)
tich(a,b)
thuong(a,b)
luythua(a,b)
laydu(a,b)
	

