'''List items are ordered, changeable, and allow duplicate values.'''
from operator import indexOf
#from .Fullname import Fullname
My_list=['ვაშლი', 'ბალი', 'ატამი', 'ლეღვი', 'ბანანი', 'ლეღვი']

print(len(My_list)) #sigrdze 6
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets

""" Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
__contains__ Return True if element is in list 
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list """

# My_list.append('ჟოლო')
# print(My_list) #['ვაშლი', 'ბალი', 'ატამი', 'ლეღვი', 'ბანანი', 'ლეღვი', 'ჟოლო']
# My_list.clear()
# print(My_list) #[]
My_list2=My_list.copy()
My_list2.append('მარწყვი')
print(My_list, My_list2) # მარტო მეორეშია მარწყვი
print(My_list.count('ლეღვი')) # 2
print("bolos tsina elementia: {0}".format(My_list[-1])) 

appendableList=['ბანანი', 'ავოკადო', 'ქლიავი'] 
My_list2.extend(appendableList)
print(My_list2) # ['ვაშლი', 'ბალი', 'ატამი', 'ლეღვი', 'ბანანი', 'ლეღვი', 'მარწყვი', 'ბანანი', 'ავოკადო', 'ქლიავი']




if My_list.__contains__('ლეღვი'):
    print("Found at index {0}".format(My_list.index('ლეღვი')))
else: 
     print("Not found")


x = 3 in [1,2,5]
y = 1 in [1,2,5]
# print(x) #False
# print(y) #True
     
#print(My_list.index('ლეღვი23'))  # Gives an error     

My_list.insert(1, 'მსხალი')
print(My_list)

My_list.pop(1)
print(My_list)

# ამასთანავე უნდა დავასკვნათ რომ pop() არგუმენტის გარეშე ამოაგდებს ბოლო ელემენტს

""" if 'ლეღვი' in My_list:
    My_list.remove('ლეღვი') #ამოაგდებს პირველ ლეღვს
    print(My_list)
else: 
    print("not fount")   """  


""" print(My_list)
while 'ლეღვი' in My_list:
     My_list.remove('ლეღვი')
print(My_list)     
 """

My_list.sort() # ცარიელი მაინც არ გამოიწვევს შეცდომას
print(My_list)  


digits=[200, 564, 896, 900]

st="("
for ind, i  in enumerate(digits):
    print("index >>{0}, value >>{1}".format(ind, i))
    if ind!=len(digits)-1:
        st+="{0},".format(i)
    else:
        st+="{0})".format(i)      
print(st)

'''  Structure in  a list ver gavakeTe movubrundebi kvlav 
class Fullname:
    
    def __init__(self, first, last):
       self.first=first
       self.last=last


struct=[]
     
struct.append(Fullname('George', 'Gogiava'))
struct.append(Fullname('Gabriel', 'Gogiava'))  
struct.append(Fullname('Роналд', 'Реиган')) 
struct.append(Fullname('სოსო', 'მათიაშვილი')) 
      
print(struct[0])      
'''

'''

* * sddfgsfgfsgfgsdfgsfgsg
* ! dsdfsdsfvgsdfvbdfsbvdfb
* ? dffgdfgdfgdfgdfg


'''



