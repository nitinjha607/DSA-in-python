num1 = 11
num2 = num1

print(num1)
print(num2)

print('num1 points to = ',id(num1))
print('num2 points to ',id(num2))

num2 = 22
print(num1)
print(num2)

print('num1 points to = ',id(num1))
print('num2 points to = ',id(num2))

dict1 = {'value':11}
dict2 = dict1

print(dict1)
print(dict2)
print(id(dict1))
print(id(dict2))


dict2['value'] =22
print(dict1)
print(dict2)
print(id(dict1))
print(id(dict2))

dict3 = {'value':33}

dict2 = dict3 
print(id(dict1))
print(id(dict2))
print(id(dict3))
dict1 = dict2
print(id(dict1))
print(id(dict2))
print(id(dict3))
'''The {'value':22} is no way to access to it so this is go under garbage collection'''