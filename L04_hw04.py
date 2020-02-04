
my_list = [3, 3, 5, 2, 1, 7, 4, 7, 10]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)