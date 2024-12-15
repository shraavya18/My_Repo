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
        print("Specific use is road trip")

c=Car()
c.general_use()  #car class does not have this method, but still can be accessed bcz its parent class has that method 
c.specific_usage()