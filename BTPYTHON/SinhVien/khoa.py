class KHOA:
	def __init__ (self,makhoa,tenkhoa):
		self.makhoa = makhoa
		self.tenkhoa = tenkhoa
	
	def setMaKhoa(self,makhoa):
		self.makhoa = makhoa
	def getMaKhoa(self):
		self.makhoa

	def setTenKhoa(self,tenkhoa):
		self.tenkhoa = tenkhoa
	def getTenKhoa(self):
		self.tenkhoa

	def toString(self):
		print(self.makhoa, ' ' , self.tenkhoa)
