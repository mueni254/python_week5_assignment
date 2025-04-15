# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass representing a car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass representing a plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass representing a boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

# Subclass representing a bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")

# Function to demonstrate polymorphism
def main():
    # Create a list of different vehicles
    vehicles = [Car(), Plane(), Boat(), Bicycle()]
    
    # Iterate over the list and call the move method
    for vehicle in vehicles:
        vehicle.move()

if __name__ == "__main__":
    main()

