class Car():
    # attributes are known as variables in programming
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        #default attribute
        self.battery="200amp"
    #behaviors are fuctions in programming
    def descriptioncar(self):
        print(f"The make of car is {self.make}")
        print(f"The model of car is {self.model}")
        print(f"The year of car is {self.year}")
    def move(self):
        print(f"{self.make} is moving with the speed")
    def applyingbrake(self):
        print(f"{self.model} has applied the brake")
    def desbattery(self):
        print(f"The amp of car's battery is {self.battery}")
    def setbatterysize(self,newsize):
        self.battery=newsize
    def getbatterysize(self):
        print(f"The battery size of your car is {self.battery}")
        
#creating objects of the class
car1=Car("Honda","City", 2006)
car2=Car("Suzuki","Mehran",1991)
print(car1.make)
print(car2.model)
print(car1.descriptioncar())

#changing an attributes value
car1.make="bmw"
print(car1.make)
print(car2.applyingbrake())
print(car1.desbattery())
car1.battery="350amp"
print(car1.getbatterysize())

#changing attribute value via function
car1.setbatterysize("900amp")
print(car1.getbatterysize())