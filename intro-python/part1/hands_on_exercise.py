"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print(pi,type(pi))


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i<50:
  print(i,"less than fifty")
elif i>50:
  print(i, "greater than 50")
else:
  print(i)



# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])

if picked_fruit=="orange":
  fruit_colour="orange"
elif picked_fruit=="strawberry":
  fruit_colour="red"
else:
  fruit_colour="yellow"
  
print(fruit_colour)


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multip(x,y):
  z=x*y
  print("The multiplication of", x, " times", y , " equals",z)
 

multip(12, 96)

multip(48,17)

multip(196523, 87323)


def multip():
    x=int(input("give an integer x"))
    y=int(input("give an integer y"))
    z=x*y
    print("The multiplication of", x, " times", y , " equals",z)
 

multip()



# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",)

print("48 x 17 =",)

print("196523 x 87323 =",)
