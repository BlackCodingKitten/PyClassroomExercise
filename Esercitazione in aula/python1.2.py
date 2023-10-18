import math
def knuthGenerator(x0, m):
    a =0
    M =0
    b = 0
    if m==1:
        a = math.pi * pow(10,8)
        M = pow(2,31)
        b = 453806245
    elif m==2:
        a = pow(7,5)
        M = pow(2,31) - 1
        b = 0
    elif m==3:
        a = pow(5,13)
        M = pow(2,31)
        b = 0
    elif m==4:
        a = pow(2,16) + 3
        M = pow(2,31)
        b = 0
    else: 
        print("Error incorrect value")
    
    for i in range (100):
        x0 = (a*(x0+b))%M
        print(i+1, "):", x0)

def menu():
    print("Casual Generator:")
    print("1. Knuth's Algorithm")
    print("2 Goodman e Miller's Algorithm")
    print("3 Gordon's Algorithm")
    print("4 Leormont e Lewis' Algorithm")
    return int(input("Insert Algorithm number: "))
    



def main():
    a = menu()
    x0 = int(input("insert start value: "))
    knuthGenerator(x0, a)


if __name__ == "__main__":
    main()