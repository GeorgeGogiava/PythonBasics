
"""
x=1              #int 
y=2.34           #float
z="giorgi"       #str
is_cool=True     #bool
x,y,z,is_cool=(1,2.34,"giorgi", True)
print("ჩემი სახელია ", z)
print (type(x))   #<class 'int'>
print(bool(1), str(True), bool(0), bool("34")) """

""" 



name, age=("George", 51)
print(f"ჩემი სახელია {name}, ჩემი ასაკია {age}") 
"""
#print(s.capitalize(), s.upper(), s.lower(), s.swapcase())
""" s, s1=("hello world", "პითონი კარგია")
print(len(s), len(s1))

d="ჩემი სახელია გიორგი"
print(d.replace('ი', 'i'))

print(d.count('ი'),d.count('ი',4),d.count('ი',12)) #4,3,2
print(d.startswith('ჩემი'), d.startswith('ჩამი'), d.endswith('გი'), d.endswith('gi') ) #True False True False """

""" 
f="My name is George"
print(f.startswith( 'My'), f.startswith('my') ) # True False
print(f.startswith( 'My'), f.lower().startswith('my') ) # True True
print(f.split()) #['My', 'name', 'is', 'George']
f="2|3|4|5|6|7|8|123"
print(f.split("9")) #"2|3|4|5|6|7|8|123"
print(f.split("")) #ValueError: empty separator """

""" from curses.ascii import isalnum

print(isalnum('12121212'), isalnum('1asa2121212'), isalnum('222.3222'), isalnum('222,3222'),isalnum('-225'))

 """

""" d="ჩემი სახელია გიორგი"
print(d.find('ი'), d.find('ი',6), d.find('ზ')) # 3 10 -1
 
g=' ___aczsdaf_____  '
print(g.strip( " _a"), len(g.strip( " _a"))) #czsdaf 6
  
"""

ff="ჩემი სახელია გიორგი"
print(ff[0:4], ff[5:11], ff[-6:], ff[5:], ff[13:100] ) # ჩემი, სახელი, გიორგი, სახელია გიორგი, გიორგი

""" conversions  int, str, float, bool 
print(float("2.36"))
name=input('შემოიტანე სახელი')
age=input('Semoitane asaki')
print(f"ჩემი სახელია {name} and my age is {age}")
"""


""" ჯამში ვღებულობთ მთლიან ტექსტს რამოდენიმე ხაზზე """
aw='''this is my multi line text
And I want to predict it
მე მგონი უნდა გადავიდეს ახალ ხაზზე
და ყველაფერი იქნება რიგზე
'''
print(aw)


# Python multiline string example using brackets 
""" ჯამში ვღებულობთ მთლიან ტექსტს ერთ ხაზზე, კარგია sql queries """

multiline_str = ("I'm learning Python. "
"I refer to TechBeamers.com tutorials. "
"It is the most popular site for Python programmers.")
print(multiline_str)

multiline_str2 = ('I\'m learning Python. '
'I refer to TechBeamers.com tutorials. '
'It is the most popular site for Python programmers.')



""" STRING FORMAT """

dstr="My name name is {} and I am {}".format('George', 52)
dstr="My name name is {0} and I am {1} and My name aslo is {0}".format('George', 52)
dstr="My name name is {n} and I am {a} and My name aslo is {n} other variant".format(n='George', a=52)
dstr="am teqstshi gamoyenebulia figuruli frcxilebi {{{0}}}".format(2022)
print(dstr) #am teqstshi gamoyenebulia figuruli frcxilebi {2022}
 
# შესაძლებელია აგრეთვე მიენიჭოს None (იგივეა რაც nothing or null)   
fr=None
print(fr is None) #True
print(fr is not None) #False