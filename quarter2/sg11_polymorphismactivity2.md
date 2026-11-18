# Duck Typing and Polymorphism

## 1. Answer the following questions

**a. What is duck typing, as explained in the video?**

Duck typing is when python does not care where a method comes from as long as it fulfills what is needed, which helps code in Python more flexible as we don't need to change structure to fit method in a class.

**b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?**

The car class needed the same method such as move() or the method being used by both Dog and Cat so it fits in the same loop.

## 2. Python Implementation

```python
# We create the car class
class Car:
    def move(self): # The move method is created that all classes use in common
        print("The car drives on the road.") # A context specific output for car

# I create the boat class
class Boat:
    def move(self): # Boat uses the same move class name so it can fit in the same function
        print("The boat sails on water.")

# I create the drone class
class Drone: # The same name for the method as both Boat and Car classes
    def move(self):
        print("The drone flies in the sky.")

# I create the start_trip function
def start_trip(vehicle): 
    vehicle.move() # This function streamlines the output

# The objects are created specifically for car boat and drone
car1 = Car()
boat1 = Boat()
drone1 = Drone()

# The start_trip function is called for all objects
start_trip(car1)
start_trip(boat1)
start_trip(drone1)
```

**Expected Output:**

```text
The car drives on the road.
The boat sails on water.
The drone flies in the sky.
```

## 3. How does the code in 2.2 demonstrate polymorphism?

The code shows polymorphism as the methods shows multiple forms. The method used in all 3 objects do different things but still serve the same purpose. The strat_trip function works with all 3 different classes without knowing its specific types. This shows how different objects can share the same method while having different behaviors.
