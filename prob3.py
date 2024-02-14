def find_maximum(numbers, compare):
    maximum = numbers[0]
    for num in numbers[1:]:
        maximum = compare(maximum, num)
    return maximum

num_list = [11, 3, 1, 2223, 125]
compare = lambda x, y: x if x > y else y
result = find_maximum(num_list, compare)
print(result)