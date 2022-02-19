my_list = [1, 2, 3, 4, 5, 6, 8]

k = 3
a = my_list[k]
my_list.remove(a)
my_list.append(a)
print(my_list.pop())
print(my_list)
