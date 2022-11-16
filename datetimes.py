from calendar import month
from datetime import date, time, datetime, timedelta
from time import strftime
print(datetime.now()) #mimdinare dro 2022-08-14
print(date.today()) # imdinare tarigi  2022-08-14 23:00:15
d=date(2022,8,28)  #tarigis atskoba
drt=datetime(2022,9,8,15,15,30) #drois atskoba
dt=datetime.combine(d, time(15,7,12)) # tarigze drois mmateba
#print(dt) # gamodis tavisi droit
print("New date Time ", dt+timedelta(minutes=45)) # atskobis tarigs miemata 45 tsuti
d=d+timedelta(days=-15)
#print(d) # miigeba 15 dge gamoklebuli
d=d+timedelta(days=1,seconds=12, microseconds=23, milliseconds=12, minutes=45, hours=1, weeks=0) # xdeba marto dgis mimateba, radganac datea da ara datetime
print('d=', d) #2022-08-14
'''
********************
სხვაობის გამოთვლა
********************
'''

d2=date(2022,8,28)
print(d2-d) #14 days, 0:00:00
print((d2-d).days) #14 
dro=datetime.now()
print((datetime.now()-dt)) #-14 days, 7:44:35.428781
print((datetime.now()-dt).days) #-14, aseve sheidzleba sxva parametris ageba
print(dro.strftime("%Y-%m-%d %H:%M:%S %A")) #2022-08-14 23:47:24 Sunday

dro=datetime(2022, 8,3,12,14,4)
print(dro.strftime("%y-%m-%e %H:%M:%S  %A" )) #2022-08-14 23:47:24 Sunday


'''
strftime
%Y: Returns the year in four-digit format. In our example, it returned "2018".
%y: Returns the year in two-digit format, that is, without the century. For example, "18" instead of "2018".
%m: Returns the month as a number, from 01 to 12.
%B: Returns the full name of the month, e.g. September.
%b: Returns the abbreviature of the month, e.g. Sep.
%d: Returns two digit day of the month, from 01 to 31. In our example, it returned "07".
%e: Returns one digit day of the month, from 1 to 31. In our example, it returned "7".
%H: Returns the hour. In our example, it returned "00".
%M: Returns the minute, from 00 to 59. In our example, it returned "00".
%S: Returns the second, from 00 to 59. In our example, it returned "00".
%a: Returns the first three characters of the weekday, e.g. Wed.
%A: Returns the full name of the weekday, e.g. Wednesday.
%w: Returns the weekday as a number, from 0 to 6, with Sunday being 0.
%p: Returns AM/PM for time.
%f: Returns microsecond from 000000 to 999999.
%Z: Returns the timezone.
%z: Returns UTC offset.
%j: Returns the number of the day in the year, from 001 to 366.
%W: Returns the week number of the year, from 00 to 53, with Monday being counted as the first day of the week.
%U: Returns the week number of the year, from 00 to 53, with Sunday counted as the first day of each week.
%c: Returns the local date and time version.
%x: Returns the local version of date.
%X: Returns the local version of time.

'''

print('time is', 
      dro.year, 'წელი',
      dro.month, 'თვე',
      dro.day, 'day',
      dro.hour, 'Hour',
      dro.minute, 'minute',
      dro.second, 'second') #time is 2022 წელი 8 თვე 15 day 0 Hour 4 minute 37 second


'''kviris dgeebi'''

print(date.today().weekday()) # 0>>orshabati    6>> kvira
