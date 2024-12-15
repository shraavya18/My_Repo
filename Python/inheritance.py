class Vehicle:
    def general_use(self):
        print("Transportation")

class Car(Vehicle):   #class car extends vehicle - car is child  and vehicle is parent 
    def __init__(self):
        print("I am a car")
        self.wheels=4
        self.has_roof=True
    
    def specific_usage(self):
        print("Specific use is commute to work")

class MotorCycle(Vehicle):
     def __init__(self):
        print("I am a Motor Cycle")
        self.wheels=2
        self.has_roof=False
    
     def specific_usage(self):
        self.general_use()  #can be called like this also if you want 
        print("Specific use is road trip")

class Bus(Vehicle):
    def general_use(self):
        print("Overriding the general use method from parent class for bus ")  #the methods from parent class can overridden in the sub class

c=Car()
c.general_use()  #car class does not have this method, but still can be accessed bcz its parent class has that method 
c.specific_usage()

m=MotorCycle()
c.specific_usage()

b=Bus()
b.general_use()

print(isinstance(c, Car))  #will check if c is object of class Car or not 
print(isinstance(m, Car))     #returns false since m is not an object of class Car 
print(issubclass(Car, Vehicle))  #will check if Car is subclass of vehicle or not 
print(issubclass(Car, MotorCycle)) #return false since car is not subclass of motorcycle 