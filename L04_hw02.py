
my_list = [5, 9, 1, 6, 2, 7, 4, 17, 5, 26]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]

print(my_list)
print(my_new_list)
