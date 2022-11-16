import math
import random
import const
# from math import sqrt, pow
# pow(4,3) არ სჭირდება 

print(3**4) #81
print (math.sqrt(25)) #5
print (math.pow(5,3)) #125.0
print(math.pi)
print(math.e)
print(math.sin(30 * math.pi/180)) #0.5
print(math.floor(2.1), math.floor(2.9), math.floor(-2.1), math.floor(-2.9)) # 2,2, -3, -3
print(math.ceil(2.1), math.ceil(2.9), math.ceil(-2.1), math.ceil(-2.9)) # 3,3, -2, -2
print(math.factorial(5)) #120
print(math.fmod(15, 2 ) ) # ნაშთი   1 
print( 15 % 4) # ნაშთი   3 
print(math.remainder(20,3))
print(math.fabs(-9.23), math.fabs(9.23), math.fabs(0)) #9.23, 9.23 0
#help("math")
print(random.random()) # 0-1 farglebshi
print(random.randint(10,25)) # mTeli ricxvi range-shi
print(random.uniform(20,30)) # abrunebs floats
print(random.randrange(20,30, 2)) # me-2 argumenti aris biji, anu iqneba sum lutsi

print(hex(255)) #'0xff'
print(hex(-42)) #'-0x2a'

print(bin(12)) # 0b1100
print(int(0b1100)) # 12

number=5.1264
print(
    "rounded= ",
    round(number, 2)
    )


fs="my name is {0} and my age is {1}".format(const.MYNAME, const.MYAGE)
print(fs)

