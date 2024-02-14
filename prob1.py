from functools import reduce
num = 1234
num_list = [int(digit) for digit in str(num)]

numsum = reduce(lambda x, y: x + y, num_list)
print(numsum)