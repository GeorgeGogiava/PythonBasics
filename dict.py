""" Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered, changeable and do not allow duplicates. """

# simple dictionary
"""
a={
    'b': 'airlane', 
    'c': 'cool', #this will be overwritten
    'c':'Cargo'  #replaces the old one
   } 
print(a['b']) #airlane
a['d']=[3,5,6] # add new
a['b']='baloon' #update Key
print(a['d'][1]) #5
print(a) # {'b': 'baloon', 'c': 'Cargo', 'd': [3, 5, 6]}
#print(a['df']) # ERROR OCCURS  
"""

# key sheidzleba ikos aseve tuplec
""" 
d = {(1, 1): 'a', (1, 2): 'b', (2, 1): 'c', (2, 2): 'd'}
d[(1,1)] #'a'
d[(2,1)] # c'
"""

#check if key exists
""" 
d = {"key1": 10, "key2": 23}

if "key1" in d:
    print("Key Exists")
else:
    print("Key doesn't exists")  
"""   


# iterate between keys
""" 
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
    print(key, a_dict[key]) 
    
"""  
 
 # iterate between values
""" 
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'} 
for value in a_dict.values():
    print(value)   
"""
  
  
# iterate between keys and values
""" 
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key, value in a_dict.items():
    print(key, '->', value)    
"""
       

# Modify the values 10% discount
""" 
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for k, v in prices.items():
    prices[k] = round(v * 0.9, 2)  # Apply a 10% discount
print(prices) 
"""
#{'apple': 0.36, 'orange': 0.32, 'banana': 0.23}
    
   
# remove the key    
""" 
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for key in list(prices.keys()):  # Use a list of a keys
    if key == 'orange':
         del prices[key]  # Delete a key from prices
print(prices)     #{'apple': 0.4, 'banana': 0.25}       

#other delete methods
del dict['Name'] # remove entry with key 'Name'
dict.clear()     # remove all entries in dict
del dict         # delete entire dictionary

"""

# key, value ადგილების შეცვლა  
""" 
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {}
for key, value in a_dict.items():
    new_dict[value] = key
print(new_dict) #{1: 'one', 2: 'two', 3: 'thee', 4: 'four'}
"""

# key, value ადგილების შეცვლა II magari meTodi
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {value: key for key, value in a_dict.items()}



# FILTER
""" 
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict ={}
for k, v in a_dict.items():
    if v>2:
        new_dict[k]=v
print(new_dict)   #{'thee': 3, 'four': 4}   
""" 

# FILTER  II metodi magaria
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {k: v for k, v in a_dict.items() if v <= 2}
print(new_dict) #{'one': 1, 'two': 2}

# create dictionary from two lists
""" 
objects = ['blue', 'apple', 'dog']
categories = ['color', 'fruit', 'pet']
a_dict = {key: value for key, value in zip(categories, objects)}
print(a_dict)
#{'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}  
""" 

# calculations
""" 
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
total_income = sum([value for value in incomes.values()])
print(total_income) #14100.0 
"""

# Sort
""" 
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
sorted_income = {k: incomes[k] for k in sorted(incomes)}
print(sorted_income) #{'apple': 5600.0, 'banana': 5000.0, 'orange': 3500.0}
 """

# Iterate trough Sort
"""
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
for key in sorted(incomes):
    print(key, '->', incomes[key]) 
"""



# returns the length of dictionary
'''
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': [4,7,8]}
print(len(a_dict))  # 4
'''

 # convert dictionary to string and vice verca
from ast import literal_eval 
 
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': [4,7,8]}
print(str(a_dict)) # {'one': 1, 'two': 2, 'thee': 3, 'four': [4, 7, 8]}

#!!!!! მაგარია   ტექსტიდან დიქშინერის შემოყვანა
b_str="{'one': 1, 'two': 2, 'thee': 3, 'four': [4, 7, 8]}"
b=literal_eval(b_str)
print(b['thee']) #3
print(b['four']) #[4, 7, 8]

#!!!!! მაგარია   JSON-დან დიქშინერის შემოყვანა
# კეიც და ვალუეც უნდა იყოს

import json
json_str=('{'
    '"name":"George",'
    '"age":"52",'
    '"IsGeorgian": "True"'          
    '}')

json_dict = json.loads(json_str)
print(json_dict['age']) #52


#import json VARIANTI TU ROGOR UNDA gadavaqciot sasurvel jsonad rom gardaqmnas

s = "{'muffin' : 'лолз', 'რადიო' : 'kitty'}"
json_acceptable_string = s.replace("'", "\"")
d = json.loads(json_acceptable_string)
print(d)
# d = {u'muffin': u'lolz', u'foo': u'kitty'}



#!!!!! მაგარია   JSON-ად გადაქცევა
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': [4,7,8]}
json_object = json.dumps(a_dict, indent = 4) 
#json_object = json.dumps(a_dict) 
print(json_object)


# ori dictioneris damateba
dict = {'Name': 'Zara', 'Age': 7, 'fruit':'apple'}
dict2 = {'Sex': 'female', 'fruit':'cherry' }

dict.update(dict2)
print ("updated dict : ", dict)
# {'Name': 'Zara', 'Age': 7, 'fruit': 'cherry', 'Sex': 'female'}



# My good example
"""
from datetime import date
weekdays=['0_mon', '1_tue', '2_wed', '3_thi', '4_fri', '5_sat', '6_son']
ye, sums=2022, {}
for m in range(1,13):
    dt=date(ye,m,1)
    new_key=weekdays[dt.weekday()]
    if new_key in sums:
        sums[new_key]+=1
    else:
        sums[new_key]=1
      
    # ძალიან მაგარი რაღაცაა, ეს აწყობს ჯერ მნიშვნელობებით desc მერე გასაღებებით asc  
out = dict(sorted(sums.items(), key=lambda item: (-item[1], item[0])))  
        
for key, value in out.items():
    print(key, '->', value) 
"""


# Checking if a dictionary is empty by checking its length
""" 
empty_dict = {}
if len(empty_dict) == 0:
    print('This dictionary is empty!')
else:
    print('This dictionary is not empty!')
# Returns: This dictionary is empty! 
# """


def get_all(**values): # გადაიქცევა სლოვარად 
    print(type(values)) # <class 'dict'>
    for k,v in values.items():
        print("{} ={}".format(k,v))
s = get_all(a=3,b=5,c=7,d=34)   



def get_sum(*values): # გადაიქცევა tuple
    print(type(values)) #<class 'tuple'>
    s=0
    for v in values:
        s+=v
    return s    
print('**************************')
s = get_sum(3,5,7,10,10)   
print(s)


# comprehension синтаксис,
