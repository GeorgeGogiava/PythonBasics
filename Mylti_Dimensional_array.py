""" init 
a = [[1, 2, 3], [4, 5, 6]]
print(a[0]) # 1,2,3
print(a[1]) # 4,5,6 
print(a[0][2]) # 3
"""

""" iteration  """
# version I
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=', ')
    print()


# version II    
""" a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()    
"""

# version III 
for row in a:
    print(' '.join([str(elem) for elem in row]))


''' Sum '''
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
print(s)

# version II
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for row in a:
    for elem in row:
        s += elem
print(s)


''' Creating list with Generators '''

a=[ i**2 for i in range(5)]
print (a, end=' ')

# Creates a list containing 5 lists, each of 8 items, all set to 0
w, h = 8, 5;
Matrix = [[0 for y in range(h)] for x in range(w)] 
Matrix = [[x*y for y in range(h)] for x in range(w)] 

print(Matrix[0])  # 0 0 0 0 0  5-jer
'''
Matrix[0][0] = 1
Matrix[0][6] = 3 # error! range... 
Matrix[6][0] = 3 # valid
'''
print(Matrix)

d,s=[7,9,10,11],0

for i in range(len(d)):
    s+=d[i]
print(s)    

print('________________________________________\n')
#t=[[],[],[],[],[],[],[],[],[],[],[]]

# igive variantia


t=[]
for i in range(11):
	t.append([])


for x in range(11):
   for y in range(11):
       t[x].append(x*y)
print(t)     


print('________________________________________\n')
#To create an empty 2d list of size n
'''
l=[]
for i in range(11):
	l.append([])
#To create an 2d list of size rows and columns
l=[[0 for j in range(11)]for i in range(11)]
print(l)

'''

b = [['a']*5]*3
#[['a', 'a', 'a','a','a'], ['a', 'a', 'a','a','a'], ['a', 'a', 'a','a','a']]
print(b) 