'''Every Data Structure are created using classes'''

class Cookie:  # Empty Cookie
    def __init__(self,color): # Constructor
        self.color = color
    def get_color(self):
        return self.color 
    def set_color(self,color):
        self.color = color   

'''Here Cookie is our own data type just like int() and str()'''
cookie_one = Cookie('green') # Green Color Cookie 
cookie_two = Cookie('blue')  # Blue Color Cookie      


print(cookie_one)
print(cookie_two)

print('Cookie one is',cookie_one.get_color())
print('Cookie two is',cookie_two.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now',cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())


'''Creating Linked List Data Structure '''
class LinkedList:
    def __init__(self,value):
        pass
    def append(self,value):
        pass
    def pop(self):
        pass
    def prepend(self,value):
        pass
    def insert(self,index,value):
        pass
    def remove(self,index):
        pass