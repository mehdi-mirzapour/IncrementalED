import numpy as np

x = np.array(range(5)) + 20

target = 30

def check(arr, num):
    return any(arr[arr==num])



print(check(x, target))
