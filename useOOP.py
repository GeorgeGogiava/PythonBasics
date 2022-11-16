
from OOP import Car2,Country, Counter1

c=Car2('Mersedes', 4)
print(c.toString())


#აქ ხდება სტრუქტურის დაგროვება მასივში
a=[]
a.append( Country('Russia', 'Moscow'))
a.append( Country('Georgia', 'Tbilisi'))
a.append( Country('Armenia', 'Erevan'))

print(a[0]) #<OOP.Country object at 0x000001B8CF9BBF70>
print("Country-{}, Capital-{}".format(a[1].name, a[1].capital )) #Country-Georgia, Capital-Tbilisi


c=Counter1()
c._current=200
c.increment()
print(c.value())
