class Calculator():
	def add(self,a=0,b=0):
		return a + b

	def sub(self,a=0,b=0):
		return a - b


if __name__ == '__main__':
	c = Calculator()
	r_add = c.add(3,8)
	print(r_add)
	r_sub = c.sub(7,5)
	print(r_sub)