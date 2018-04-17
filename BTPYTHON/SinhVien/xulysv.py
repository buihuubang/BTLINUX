from sinhvien import sinhvien 
from khoa import KHOA

n = int(input("Nhap so phan tu mang:")

list_sv = [None] * n

i = 0
while i < n:
	mssv = input("Nhap mssv:")
	hoten = input("Nhap ho ten:")
	khoa = input("Nhap khoa:")
	sv = sinhvien(mssv,hoten,khoa)
	list_sv.append(sv)
	i += 1

j = 0
while j < n:
	list_sv[j].toString()
	j += 1


