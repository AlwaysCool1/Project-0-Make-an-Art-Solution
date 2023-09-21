from turtle import *
setup()
x = float(input("Enter a Value for X Between -100.0 and 100.0\n"))

if -100.0 <= x <= 100.0 :
     print ("Your X value is ", x)
else:
     print ("Please re-run the program and enter a value between 0.0 and 100.0\n")
     exit()
y = float(input("Enter a Value for Y Between -100.0 and 100.0\n"))
if -100.0 <= y <= 100.0 :
     print ("Your Y value is ", y)
else:
     print ("Please re-run the program and enter a value between 0.0 and 100.0\n")
     exit()
    
          
def circles (radius, colour):
    penup()
    pencolor (colour)
    goto (0,radius)
    pendown ()
    setheading (180)
    circle (radius)
    penup()


circles (100, "black")

def hexagon (size_length):
    pendown ()
    forward(size_length)
    right (60)

goto (x, y) 
for _ in range (6):
    hexagon (50)             

exitonclick ()


for i in range(2):
  turtle.forward(100)