class My_matrix:
	def __init__(self, list_):
		self.list_ = list_
		

	def longe(self):
		return len(self.list_)

	
	def digit(self):
		for i in range(len(self.list_)):
			a = len(self.list_[0]) 
			a += len(self.list_[i])
		return a


m = My_matrix([[1, 3, 4], [1, 5, 7]])
print(m.digit())