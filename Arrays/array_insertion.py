import array
my_array1 = array.array('i',[1,2,3,4])
print(my_array1)
my_array1.insert(0,6) # O(n)- time complexity and O(1) - space complexity
print(my_array1)
my_array1.insert(2,6)
print(my_array1)
my_array1.insert(4,6)
print(my_array1)