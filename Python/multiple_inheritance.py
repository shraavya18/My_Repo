#Unlike Java, python supports multiple inheritance

class Father():
    def gardening(self):   
        print("I enjoy gardening")

    def skills(self):
        print("Fathers skills are Programming")
    
class Mother():
    def cooking(self):
        print("I enjoy cooking")
    
    def skills(self):
        print("Mothers skills are art")

class Child(Father, Mother):
    def sports(self):
        Father.skills(self) #will print fathers skills  - these two will come under sports() method only 
        Mother.skills(self)        #will print mothers skills 
        print("I enjoy sports")

c=Child()
c.gardening()    #gardening and  cooking are two different methods so no conflict 
c.cooking()
c.sports()
c.skills()  #conflicting method - skills() is in both father and mother class and it is not specified from which class it should take  
                    #it takes fathers by default bcz father is definied first 

