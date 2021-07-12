from matrices import Matrices

a = Matrices([[1,2,3],[4,5,6]], [[7,8,9], [10,11,12]])

print('\nMatrices:')
print('matrix 0:', a.matrix0)
print('matrix 1:', a.matrix1)

print('\nShape:')
print('shape 0:', a.shape0)
print('shape 1:', a.shape1)

print('\nOperations:')
print('add:', a.add())
print('subtract:', a.subtract())
print('multiply:', a.multiply())
print('tensordot:', a.tensordot())
