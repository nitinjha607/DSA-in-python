from array import *
arr1 = array('i',[1,2,3,4,5])
def accessElement(array,index):
    if index > len(array):
        print("There is not any element in this index")
    else:
        print(array[index])
accessElement(arr1,0) # Accessing first element
accessElement(arr1,8) 
# Time Complexity: O(1) - because we are accessing the element directly using its index
# Space Complexity: O(1) - because we are not using any extra space
# In this code, we are using the array module to create an array of integers.
# We define a function accessElement that takes an array and an index as arguments.
# The function checks if the index is greater than the length of the array.
# If it is, it prints a message indicating that there is no element at that index.
# If the index is valid, it prints the element at that index.
# The function is then called twice, once with a valid index and once with an invalid index.