# O(2n) == O(3n) == O(4n) ..... == O(n)

def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)    

print_items(10)
