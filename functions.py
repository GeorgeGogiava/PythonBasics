
'''Simple function 
def My_function(x):
    return x ** 3

print(My_function(5))  #125 
'''


'''
def my_function(*kids):
  print(kids)  #('Emil', 'Tobias', 'Linus')
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
'''

'''
def my_function(kids): #ase sheidzleba listis gadacema არ უნდა ფრჩხილები II varianti
  print(kids)  #('Emil', 'Tobias', 'Linus')
  print("The youngest child is " + kids[2])

my_function(["Emil", "Tobias", "Linus"])
'''

''' # ასე შეიძლება არგუმენტების გადაცემა სხვადასხვა თანმიმდევრობით
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
'''


'''  როდესაც ეგზავნება უცნობი რაოდენობის კეივორდები **kwargs
def my_function(**kid):
  print(kid) #{'fname': 'Tobias', 'lname': 'Refsnes'}
  print("His last name is " + kid["lname"]) #His last name is Refsnes
my_function(fname = "Tobias", lname = "Refsnes")
'''

'''  საგულისხმო მნიშვნელობები
def my_function(country = "Norway"):
  print("I am from " + country)
'''

''' 
def my_function(b, a=4): # საგულისხმო მნიშვნელობები უნდა იყოს ბოლოში, როგორც 
  return a+b
print(my_function(7)) #11
''' 


''' 
def myfunction():
  pass  #აგვაცილებს შეცდომას, როცა არ არის აღწერილი

#print(myfunction) თუ გამოვიძახებთ გამოიტანს შეცდომას
''' 


'''ძალიან მაგარია შეიძლება ფუნქციამ დააბრუნოს რამდენიმე მნიშვნელობები ცვლის პარaმეტრის გადაცემას Byreference
def square(a):
    return a**2, a*4
fartobi, perimetri =square(9)
print(fartobi, perimetri) #81, 36
'''


'''ძალიან მაგარია შეიძლება ფუნქციიდან დაბრუნებული მნიშვნელობა კიდეც შეამოწმო და კიდეც მიანიჭო
#ამით თავიდან ვირიდებთ ფუნქციის ორჯერ გამოთვლას
def square(a):
    return a**2

if (s:=square(16))<100:
    print("farTobi naklebia 100-ze da aris {0}".format(s))
else:
    print("farTobi metia 100-ze da aris {0}".format(s))     
    
'''



""" # ასე შეიძლება ფუნქციაზე ახსნის გაკეთება
def r(lname, fname):
  '''
  აქვს ორი პარამეტრი: ლნამე: სახელი და ფნამე გვარი
  აბრუნებს ჰელლოწ
  \nSeiZleba hqondes Semdegi mniSvnelobebi:
  short, large, m2, m3
  \nfnme: SeiZleba hqondes Semdegi mniSvnelobebi: 
  1111, 2222, 33333 da a.S.
  '''
  print("hello {0} {1}!".format(lname, fname))
   """


#ასე ხდება ტიპების მიცემა
def pick(l: list, index: int) -> int:
    if not isinstance(index, int): raise TypeError
    return l[index]
  
print(pick(['a', 'b', 'c'],True))
 