class sinhvien:
	def __init__(self,mssv,hoten,khoa):
		self.mssv = mssv
		self.hoten = hoten
		self.khoa = khoa

	def setMSSV(self,mssv):
		self.mssv = mssv
	def getMSSV(self):
		return self.mssv

	def setHoTen(self,hoten):
		self.hoten = hoten
	def getHoTen(self):
		return self.hoten

	def setKhoa(self,khoa):
		self.khoa = khoa
	def getKhoa(self):
		return self.khoa

	def toString(self):
		print(self.mssv,' ',self.hoten,' ',self.khoa)
