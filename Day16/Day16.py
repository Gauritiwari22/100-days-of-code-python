"Day 16"
#OOP( Object Oriented Programming)
#OOP is a way of programming where you create objects that contain both data and the functions that work on that data.
# It exists because large programs become impossible to manage without structure.
# OOP helps with:

# organizing complex systems
# maintaining and updating code
# working in teams

# Class
# A class is a blueprint or template for creating objects.
# It tells what data an object will have and what actions it can perform

# Objects
# An object is a real instance created from a class.
# If class is the plan then object is the actual thing you use.

# A class defines what an object can do and can have.
# The object is what actually does those things.

class Car:               # Car is the class
    def start(self):        # start() is the method
        print("Car has started")

my_car = Car()       # my_car is the object created using the class and its attributes
my_car.start()

from turtle import Turtle,Screen

mathew=Turtle()
print(mathew)
mathew.shape("turtle")
mathew.color("DeepPink")
mathew.forward(100)
mathew.degrees(90)

my_screen=Screen()
my_screen.exitonclick()



from prettytable import PrettyTable

table=PrettyTable()
table.add_column("Name",["Gauri","Gunika","Kajal"])
table.add_column("Marks",["100","87","90"]) # method
print(table)
table.align="l" # editting attribute value



