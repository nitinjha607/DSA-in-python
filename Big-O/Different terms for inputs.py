def print_items(a,b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)    

print_items(4,4) # O(a+b)

def print_items(a,b):
    for i in range(a):
        for j in range(b):
            print(i,j)

print_items(3,4) # O(a*b)