
# Creation of ll using dictionary 11 -> 3 -> 23 -> 7 -> 4
head = {
    'value':11,
    'next':{
        'value':3,
        'next':{
            'value':23,
            'next':{
                'value':7,
                'next':{
                    'value':4,
                    'next': None
                        }
                  }
            }
      }
}

print(head['next']['next']['value'])
# This will only run with a linked list 
# print(my_ll.head.next.next.value)