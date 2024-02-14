words = ['watermelon', 'banana', 'apple', 'orange', 'pineapple']
sorted_list = sorted(words, key=lambda x: (len(x), x))

print(sorted_list)