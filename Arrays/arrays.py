import array # First module to create an array
my_array = array.array('i')
print(my_array)
my_array1 = array.array('i',[1,2,3,4])
print(my_array1)

import numpy as np # Second module to create an array
np_array = np.array([],dtype = int)
print(np_array)

np_array1 = np.array([1,2,3,4],dtype = int)
print(np_array1)