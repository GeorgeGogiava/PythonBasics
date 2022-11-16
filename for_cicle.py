import datetime


for i in range(11):
    print("{0}-ის კვადრატია {1}".format(i, i**2))
    
    
for i in range(10,21):
    print("{0}-ის კვადრატია {1}".format(i, i**2))
    
    
xmovani, tanxmovani=0,0
for s in "saqartvelo":
    if s=='a' or s=='e' or s=='i' or s=="o" or s=='u':
        xmovani+=1
    else: tanxmovani+=1        
print("ხმოვანი- {0}{1}თანხმოვანი-{2}".format(xmovani, '\n', tanxmovani))    

    
is_xmovani=False
for s in "sqwe": 
     if s=='a' or s=='e' or s=='i' or s=="o" or s=='u': 
         is_xmovani=True
         break  

print(f"is_xmovani={is_xmovani}")    


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 
  
for x in range(2, 30, 3): # 3 aris biji
  print(x) 
  
for x in range(6):
  print(x)
else: #roca cikli mtavrdeba
  print("Finally finished!") 
  

for x in range(6):
  if x == 3: break
  print(x)
else: # breakis dros ar mushaobs
  print("Finally finished!")
 
  
''' ormagi cikli'''  
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)  


weekdays, marxva =['ორშ', 'სამ', 'ოთხ', 'ხუთ', 'პარ','შაბ', 'კვი'], 0
ye=input('შემოიტანე წელი')
for i in range(1,13):
    dt=datetime.date(int(ye), i,14)
    print ("{0} >> {1}".format(dt.strftime("%y-%m-%e"), weekdays[dt.weekday()]))
    if dt.weekday()==2 or dt.weekday()==4: 
        marxva+=1 
print(f"marxvis dgeebia >>{marxva}")   


for mon in range(9,13):
    for day in range(6,15):
        dt=datetime.date(2022, mon, day)
        if dt.weekday()==6 or dt.weekday()==5:
           print ("{0} >> {1}".format(dt.strftime("%y-%m-%e"), weekdays[dt.weekday()]))
        if dt.weekday()==6:
            break  
        

'''მაგალითი იმისა თუ როგორ უნდა ვაკონტროლოთ ინდექსი, უნდა გამოვიყენოთ enumerate, ჯერ იწერება ინდექსი'''

digits=[200, 564, 896, 900]

st="("
for ind, i  in enumerate(digits):
    print("index >>{0}, value >>{1}".format(ind, i))
    if ind!=len(digits)-1:
        st+="{0},".format(i)
    else:
        st+="{0})".format(i)      
#print(st) # (200,564,896,900)      


text = ['Python', 'is', 'a', 'fun', 'programming', 'language']
# join elements of text with space
print(' '.join(text))
# Output: Python is a fun programming language

                                                                       