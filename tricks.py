""" 
'''
1)   2 განზომილებიანი ლისტის 1 განზომილებიანად გარდაქმნა 
'''

import itertools
a=[[1,2], [3,4], [5,6], [7,8,9,10]]
b=list(itertools.chain.from_iterable(a))
print(b) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""


"""
'''
2)    REVERSE A LIST
'''
a=["10", "9", "8", "7"] #  or a=[2.36, 5.5, 1.36, 2.36, 4.56]
print(a[::-1]) # ['7', '8', '9', '10'] requires when not want to copy list, instead only show 
print(a) # ['10', '9', '8', '7'] previous list remains unchanged 
"""


""" 
'''
3)   COMBINING DIFFERENT LISTS
'''
a, b, c=['a', 'b', 'c', 'd'], ['1','2','3','4'],  ['10','20','30']
for x,y,z in zip(a,b,c):
    print(x,y,z)
  
#a 1 10
#b 2 20
#c 3 30  
# umoklesi masivis amotsurvamde 
 """


'''
4)  Launch web server
# python -m http.server 7000
# http://localhost:7000/tuple.py # zustad ar vici 

'''


'''
5)  Swap
'''
"""
a,b=3,5
a,b =b,a
print(a,b) # 5,3
"""

'''
6)  ვებ-საიტის გახსნა
'''
#import webbrowser
#webbrowser.open('http://gogiava.com.ge/calendar.php', 1) 


'''
7)  ორი ლისტიდან რომლები არ არის საერთო მათი გამოტანა
'''
"""
a, b=['a', 'b', 'c', '1', '2', '3', '5'],  ['a', 'd', 'b', 'c', '4', '1', '2', '3' ]
#c=list(set(b)-set(a)) # ['d', '4'] 
c=list(set(a)-set(b)) # ['5']
print(c) 
"""

'''
8)  რა ადგილს იკავებს მეხსიერებაში
'''
"""
import sys, datetime
a, b, c, d, e, n, f, s, s1=12, 58361, [2, 'aaaa'], datetime.datetime.now(), True, None, 2.36, 'a', 'ას'
print(sys.getsizeof(a), sys.getsizeof(b), sys.getsizeof(c), sys.getsizeof(d), sys.getsizeof(e),  sys.getsizeof(n), sys.getsizeof(f), sys.getsizeof(s), sys.getsizeof(s1))
#28 28 72 48 28 16 24 50 78
 """
 
'''
9)  მატრიცის გადმოტრიალება შესაბამისი ინდექსების აღება
'''

mat=[[1,2,3], [4,5,6], [7,8,9]]
new_mat=zip(*mat)

for row in mat:
    print(row)

for row in new_mat:
    print(row)

#[1, 2, 3]  #list
#[4, 5, 6] 
#[7, 8, 9]
    
#(1,4,7)    #tuple
#(2,5,8)
#(3,6,9)    