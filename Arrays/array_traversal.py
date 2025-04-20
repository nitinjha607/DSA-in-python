from array import *

arr1  = array('i',[1,2,3,4])
arr2  = array('d',[1.3,1.5,1.6])

def TraversalArray(array): # Time Complexity - O(n) and Space Complexity - O(1)
    for i in array:
        print(i)

TraversalArray(arr1)