"""
#M03: Custom Data Class
#C.J. Becker
#2/12/2024
#Python 3.8.10
$make a class, I made it represent a water bottle
"""

class waterBottle():
    ##water will go from 0 to 100, lid will have 2 values to say if it's open or not
    #default values are set, but can be changed when called with parameters
    def __init__(self, waterAmount = 1000, lidStatus = 0):
        self.water = waterAmount
        self.lid = lidStatus
        
    #return amount of water
    def getWater(self):
        return self.water
    #print if lid is on or off
    def printLid(self):
        if(self.lid == 0):
            print("The lid is on the bottle")
        else:
            print("The lid is off the bottle")
    #put the lid on or take the lid off
    def lidChange(self):
        if(self.lid == 0):
            self.lid = 1
        else:
            self.lid = 0
    #add water to the bottle, maxed out at 1000, cannot fill when lid is on
    def fillBottle(self, waterNumber = 0):
        if(self.lid == 1):
            if(self.water + waterNumber > 1000):
                self.water = 1000
            else:
                self.water += waterNumber
        else:
            print("You cannot fill the bottle")
            self.printLid()
    #drink water from the bottle, maxed out at 0, cannot drink when lid is on
    def drinkWater(self, waterNumber):
        if(self.lid == 1):
            if(self.water - waterNumber < 0):
                self.water = 0
            else:
                self.water -= waterNumber
        else:
            print("You cannot drink from the bottle")
            self.printLid()
            
    def __str__(self):
        print("This is a water bottle")
    def __eq__(self, other):
        if(self.water == other.water and self.lid == other.lid):
            return True

def main():        
    b1 = waterBottle()
    print(f"There are {b1.getWater()} ml of water in the first bottle")
    b2 = waterBottle(50, 1)
    b1.printLid()
    print(f"There are {b2.getWater()} ml of water in the second bottle")
    b2.printLid()
    
    print(f"There are {b2.getWater()} ml of water in the second bottle")
    b2.fillBottle(300)
    print(f"There are {b2.getWater()} ml of water in the second bottle")
    b2.fillBottle(3000)
    print(f"There are {b2.getWater()} ml of water in the second bottle")
    
    
    print(f"There are {b1.getWater()} ml of water in the first bottle")
    b1.drinkWater(300)
    b1.lidChange()
    b1.drinkWater(300)
    print(f"There are {b1.getWater()} ml of water in the first bottle")
    b1.drinkWater(3000)
    print(f"There are {b1.getWater()} ml of water in the first bottle")
    
    b2.drinkWater(400)
    b2.lidChange()
    print(f"There are {b2.getWater()} ml of water in the second bottle")
    b2.fillBottle(300)
    b2.lidChange()
    b2.fillBottle(300)
    print(f"There are {b2.getWater()} ml of water in the second bottle")
    
    b3 = waterBottle()
    b4 = waterBottle()
    b3.__str__()
    print(b3.__eq__(b4))
    
if __name__ == "__main__":
    main()