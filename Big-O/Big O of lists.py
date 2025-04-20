my_list = [11,3,23,7]

my_list.append(17)
print(my_list)  # O(1)
my_list.pop()
print(my_list)  # O(1)
my_list.pop(0)
print(my_list)  # O(n)
my_list.insert(0,11)
print(my_list)  # O(n)
my_list.insert(1,'Hi')
print(my_list)  # O(n)

# If we search element in list not by index then we have to iterate through it that is O(n)
# But when we search like what is the element at index 3 then it takes O(1) time operation
'''
Big 0 :- It is a complexiity that is going to be less or equal to wrost case.
Big Omega :- It is a complexiity that is going to be at least more than best case.
Big Theta :- It is a complexiity that is within bounds of the wrost and the best case.

'''