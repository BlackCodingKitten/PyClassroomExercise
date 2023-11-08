def es1():
    print("Esercizio 1:")
    n = int(input("Inserisci un numero intero positivo: "))
    for i in range(1,n):
        print(i,"\t",int(((i)*(i+1))/2))
        
def es2():
    print("Esercizio 2:")
    max =0
    min =0
    sum =0
    for i in range (3):
        x=float(input("inserisci un numero reale"))
        if not(i):
            max =x
            min =x
        sum =sum +x
        if x>max:
           max=x
        if x<min:
            min=x
    print("Max: ", max, " Min: ",min," Sum: ",sum )

def es3():
    print("Esercizio 3:")
    max =0
    min =0
    sum =0
    for i in range (20):
        x=float(input("inserisci un numero reale"))
        sum =sum +x
        if not(i):
            max =x
            min =x
        if x>max:
           max=x
        if x<min:
            min=x
    print("Max: ", max, " Min: ",min," Sum: ",sum )

def es4():
    print("Esercizio 4:")
    max =0
    min =0
    sum =0
    x=1
    while x>0:
        x=float(input("inserisci un numero reale"))
        sum = sum +x
        if x>max:
           max=x
        if x<min:
            min=x
    print("Max: ", max, " Min: ",min," Sum: ",sum )

def es5():
    print("Esercizio 5:")
    n = int(input("Inserisci un numero intero positivo: "))
    sum =0
    for i in range(n):
        if i%2:
            sum=sum+i
    print(sum)
    
def es6():
    print("Esercizio 6:")
    x = int(input("Inserisci un numero intero positivo: "))
    fat=1
    for i in range(1,x):
        fat = 1* i
    print (fat)

def es7():
    print("Esercizio 7: ")
    n = int(input("Inserisci due numeri interi positivi: "))
    m = int(input())
    x = 0
    for i in range(m):
        x= x+n
    print(x)

def es8():
    print("Esercizio 8:")
    # n/m
    n = float(input("Inserisci due numeri naturali: "))
    m = float(input())
    if(m==0):
        print("Invalid operation")
    i=0
    if(n>0 and m>0):
        while n>0:
            n=n-m
            i=i+1
    elif(n>0 and m<0):
        while n>0:
            n=n+m
            i=i-1
    elif(n<0 and m>0):
        while n<0:
            n=n+m
            i=i-1
    else:
        while n<0:
            n=n-m
            i=i+1
    print(i)    

es8()