class Matrices:
	def __init__(self, matrix0, matrix1):
		self.matrix0 = matrix0
		self.matrix1 = matrix1

		self.shape0 = (len(matrix0), len(matrix0[0]))
		self.shape1 = (len(matrix1), len(matrix1[0]))
	
	def add(self):
		return [[self.matrix0[row][col] + self.matrix1[row][col] for col in range(len(self.matrix0[row]))] for row in range(len(self.matrix0))]

	def subtract(self):
		return [[self.matrix0[row][col] - self.matrix1[row][col] for col in range(len(self.matrix0[row]))] for row in range(len(self.matrix0))]
	
	def multiply(self):
		matrix2 = [[0 for x in range(len(self.matrix0[y]))] for y in range(self.shape0[0])]
		for x in range(self.shape0[0]): 
			for y in range(self.shape1[0]): 
				for z in range(self.shape1[0]): 
					matrix2[x][y] += self.matrix0[x][z] * self.matrix1[z][y]
		return matrix2

	def tensordot(self):
		from numpy import array, tensordot; return tensordot(array(self.matrix0), array(self.matrix1), axes=0)
