import turtle
import random

def randDirection():
    if(random.random() <= 0.5):
        return "r"
    else:
        return "l"

def randAngle():
    deg = random.uniform(-1,1)
    return deg * 30

def randomColor(x):
    a = ["black","white","gray","red","green","blue","cyan","yellow","magenta","orange","brown","pink","purple","gold","silver"]
    return a[x]

def turtleRoutine(t):
    t.forward(5)
    if(randDirection() == "l"):
        t.left(randAngle())
    else:
        t.right(randAngle())
    t.color(randomColor(int(random.random() * 15)))

def main():
    it = int(input("Iteraction number: "))
    t = turtle.Turtle()
    for i in range(it):
        turtleRoutine(t)
    t.done()
       

if __name__ == "__main__":
    main()