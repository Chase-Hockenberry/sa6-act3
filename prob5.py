def power(numbers, n):
    power_num = list(map(lambda x: x ** n, numbers))
    return power_num

num_list = [2, 3, 4, 5]
n = 3

result = power(num_list, n)
print(result)