class Vehicle:
    def __init__(self, name):
        self.type = name
   
class Bus(Vehicle):
    def __init__(self, name, fare):
        self.name = name
        self.fare = fare
        
obj = Bus("Bus", "100 Rps.")
print("The fare of the", obj.name, "is", obj.fare)
#print(issubclass(Bus, Vehicle))