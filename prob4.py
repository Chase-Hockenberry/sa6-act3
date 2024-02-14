def intersection(list1, list2):
    intersect_list = list(filter(lambda x: x in list2, list1))
    return intersect_list

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

result = intersection(list1, list2)
print(result)