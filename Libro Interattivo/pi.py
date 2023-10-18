import random 
import math

inside_square = 0
outside_square = 0

point = int(input("How many random point should we genarate?"))

for i in range(point):
    
    x=random.random()
    y=random.random()
    
    if(((x*x) + (y*y)) < 1):
        inside_square +=1
    else:
        outside_square +=1

pi = 4 * (inside_square / (inside_square + outside_square))

print("The approximation is ", round(pi,6))

diff = pi - math.pi
err = ( diff / math.pi ) * 100

print("The difference with the value of math.pi is", round(diff,6), "with error percentage of", round(abs(err),6), "%")
