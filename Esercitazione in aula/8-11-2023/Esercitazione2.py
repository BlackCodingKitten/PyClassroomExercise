
def asterischi(n):
    if n<0:
        print("N deve essere maggiore di zero!")
    for i in range(n):
        print("*", end="")

def fattoriale(n):
    if n==0:
        return 1
    return n * fattoriale(n-1)

def max_Float(max=0, i=3):
    if i==0:
        return print(max)
    else:
        x=float(input("Inserisci un numero: "))
        if x>max:
            max_Float(x,i-1)
        else:
            max_Float(max,i-1)

def somma():
    x=int(input("Inserisci un numero o -1 per teminare: "))
    if(x==-1):
        return 0
    else:
        return x+somma()
    
def mod_2_3 (v="OK"):
    x=int(input("Inserisci un numero o -1 per teminare: "))
    if(x==-1):
        return v
    elif not(x%2) or (x%3==0):
        return mod_2_3(v)
    else:
        return mod_2_3("NO")
    

def fibonacci(n):
    if n<=0:
        print("Errore!")
    prec = 1
    curr = 1
    print("1 1", end=" ")
    for i in range(n):
        print(prec+curr, end =" ")
        temp = curr
        curr = curr+prec
        prec = temp


def main():
    # asterischi(int(input("inserisci n: ")))  
    # print(fattorianle(int(input("inserisci n: "))))
    # max_Float()
    # print(somma())
    # print(mod_2_3())
    fibonacci(int(input("Inserisci n: ")))
main()