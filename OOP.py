class Car:
    num=9 # ასე შეიძლება არა ინიციალიზირებული თვისების აღწერა და შემდგომ გამოყენება toString
    def __init__(self, model, volume):
        self.model=model
        self.volume=volume
        
    def toString(self) -> str:
        return "model {0}, volume {1} sm3".format(self.model, self.num)   
    
    @staticmethod  # ასე აღიწერება სტატიკური მეთოდები
    def chessBoard():
        return "Chess Board Contains 64 cell"
    
       
    
"""
c=Car('Audi', 2.36)
print(c.toString()) # არ დაგვავიწყდეს ფრჩხილები მეთოდის ბოლოს, რომ არ გამოგვიტანოს შეცდომა <bound method Car.toString of ...
print(Car.chessBoard()) 
"""
 # ასე ხდება  Inharitance
class Car2(Car): 
    
    def newMethod(self):
        return "New Method " + Car.toString(self) # ასე ხდება მშობლის მეთოდის გამოყენება

    def toString(self):
        return "model {0}, volume {1} sm3".format(self.model, self.num) 
         

        
car2=Car2('BMW', 5.0)
print(car2.toString())    #model BMW, volume 19 sm3 
print(car2.newMethod())  


class Country:
    def __init__(self, name, capital) -> None:
        self.name=name
        self.capital=capital
 
        
class Counter1:
    def __init__(self):
        self.__current = 0
        self.name="George"

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current

    def reset(self):
        self.__current = 0

    @property
    def ChangeName(self):
        self.name="Gogiava"
     
     