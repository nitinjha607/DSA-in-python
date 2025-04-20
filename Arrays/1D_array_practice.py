from array import *

# 1. Create an array and traverse

my_array = array('i',[1,2,3,4,5])
for i in range(len(my_array)):
    print(my_array[i])

# 2. Access individual elements through indexes

print(my_array[0]) # Output: 1
print(my_array[1]) # Output: 2
print(my_array[2]) # Output: 3
print(my_array[3]) # Output: 4
print(my_array[4]) # Output: 5

# 3. Append any value to the array using append() method

my_array.append(6) # O(1)- time complexity and O(1) - space complexity
print(my_array) # Output: array('i', [1, 2, 3, 4, 5, 6])

# 4. Insert value in an array using insert() method

my_array.insert(0,0) # O(n)- time complexity and O(1) - space complexity
print(my_array) # Output: array('i', [0, 1, 2, 3, 4, 5, 6])

# 5. Extend the array using extend() method

my_array.extend([7,8,9]) # O(k)- time complexity and O(1) - space complexity
print(my_array) # Output: array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# 6. Add items from list into array using fromlist() method

my_array.fromlist([10,11,12]) # O(k)- time complexity and O(1) - space complexity
print(my_array) # Output: array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# 7. Remove any array element using remove() method

my_array.remove(0) # O(n)- time complexity and O(1) - space complexity
print(my_array) # Output: array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# 8. Remove last array element using pop() method
my_array.pop() # O(1)- time complexity and O(1) - space complexity
print(my_array) # Output: array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

# 9. Fetch any element through its index using index() method
print(my_array.index(5)) # Output: 4

# 10. Reverse a python array using reverse() method
my_array.reverse() # O(n)- time complexity and O(1) - space complexity
print(my_array) # Output: array('i', [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# 11. Get array buffer information using buffer_info() method
print(my_array.buffer_info()) # Output: (140703268180032, 11)

# 12. Check for number of occurrences of an element using count() method
print(my_array.count(5)) # Output: 1

# 13. Convert array to string using tostring() method
print(my_array.tostring()) # Output: b'\x0b\n\t\x08\x07\x06\x05\x04\x03\x02\x01'

# 14. Convert array to list using tolist() method
print(my_array.tolist()) # Output: [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 15. Append a string to char array using fromstring() method
my_array.fromstring('hello') # O(k)- time complexity and O(1) - space complexity
print(my_array) # Output: array('i', [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# 16. Slice elements from an array
print(my_array[0:5]) # Output: array('i', [11, 10, 9, 8, 7])