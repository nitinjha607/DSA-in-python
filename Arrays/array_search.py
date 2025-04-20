import array
my_array1 = array.array('i',[1,2,3,4])

def linear_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1
# Time Complexity: O(n) - because we are iterating through the entire array
# Space Complexity: O(1) - because we are not using any extra space
# In this code, we are using the array module to create an array of integers.
# We define a function linear_search that takes an array and an element as arguments.
# The function iterates through the array and checks if the current element is equal to the target element.
# If it is, the function returns the index of the element.
# If the element is not found, the function returns -1.
# The function is then called with the array and the target element.
print(linear_search(my_array1, 3)) # Output: 2
print(linear_search(my_array1, 5)) # Output: -1