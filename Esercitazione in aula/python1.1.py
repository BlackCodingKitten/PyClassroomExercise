import random

def sequenceGenerator(seed):
    sum = 0
    random.seed(seed)
    for i in range(20):
        x=1 + random.random()*98
        sum=sum+x
        print(round(x,2))
    return sum

def main():
    seed = int(input("Insert chosen seed: "))
    
    print("Sequence 1:")
    x1 = sequenceGenerator(seed)
    print ("Squence 2:")
    if (x1 == sequenceGenerator(seed)):
        print("Sono la stessa sequenza")


if __name__ == "__main__":
    main()