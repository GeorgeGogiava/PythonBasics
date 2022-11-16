""" A tuple is a collection variables which is ordered and unchangeable.
Tuples are written with round brackets. """
d='საზამთრო'
my_tuple=('ვაშლი', 'ბანანი', 'ბალი', 'ანანასი', d, 'ვაშლი')
my_tuple2=('ვაშლ-ატამა', 'მარწყვი')
print(my_tuple)

x,y=my_tuple2 
print(x, y)# ვაშლ-ატამა, მარწყვი 

#x,y,z=my_tuple2 # გამოიწვევს შეცდომას  not enough values to unpack (expected 3, got 2)

# თუ ერთ წევრს შეიცავს არ უნდა დაგვაწყდეს მძიმის დასმა ბოლოში
my_tuple3=('msxali',)

print(len(my_tuple2)) #2
print(type(my_tuple2)) # <class 'tuple'>

#Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(my_tuple.index('ვაშლი')) # 0 აბრუნებს 1-ad shemxvedrs


if my_tuple.__contains__('ბალი'):
    print("Found at index {0}".format(my_tuple.index('ბალი')))
else: 
     print("Not found")
     
     
this_tuple=(34, ['a', 'b'], True)
    
# CONVERTION function list, tuple
vv=list(this_tuple)
print(vv) # [34, ['a', 'b'], True]

# indexsebi mainc []-it etiteba
print(this_tuple[1]) #['a', 'b']       
print(this_tuple[0]) #34  