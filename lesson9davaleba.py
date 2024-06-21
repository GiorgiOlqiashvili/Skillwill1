# List ####################
my_list = [1, 2, 3, 4, 5, ]
my_list.append(6)
my_list.remove(3)
element = my_list[2]
length = len(my_list)


# Dictionary ###########################
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict['job'] = 'Engineer'
del my_dict['age']
name = my_dict['name']
keys = my_dict.keys()


# Tuple ############################
my_tuple = (10, 20, 30, 40, 50)

# კორტეჟის სიის ქცევა
my_list = list(my_tuple)
print("სია:", my_list)

# ელემენტების დამატება
my_list.append(60)
my_list.append(70)
print("დამატებული ელემენტები:", my_list)

# ელემენტების წაშლა
my_list.remove(20)
my_list.remove(50)
print("წაშლილი ელემენტები:", my_list)

# სიის უკან კორტეჟში გადაყვანა
new_tuple = tuple(my_list)
print("კორტეჟი:", new_tuple)

