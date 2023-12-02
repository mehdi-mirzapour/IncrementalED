import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5]])
print(twoDArray)

twoDArray = np.insert(twoDArray, 2, [[1,2]], axis=1)
print(newTwoDArray)

print(len(twoDArray))

newTwoDArray = np.append(newTwoDArray, [[1,2,3,4]], axis=0)
print(newTwoDArray)
print(len(newTwoDArray))
print(len(newTwoDArray[0]))


