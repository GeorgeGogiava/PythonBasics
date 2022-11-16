import datetime
i = 1
while i < 6:
  print(i)
  i += 1
  
  
""" Exit the loop when i is 3: """

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1  
  
  
""" Continue to the next iteration if i is 3:  """ 
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) 
  
  
""" Print a message once the condition is false: """

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6") 
  
  
d1=datetime.date(2022,8,1)

d2=datetime.date(2022,9,1)  

weekdays =['ორშ', 'სამ', 'ოთხ', 'ხუთ', 'პარ','შაბ', 'კვი']

while d1<=d2:
  print("{0} {1}.".format(d1.strftime("%d.%m.%Y"), weekdays[d1.weekday()]))
  d1=d1+datetime.timedelta(days=1)
  
  
        