
            n=n/2

def G_while():
    i=0
    n=int(input("Inserire il numero di partenza:"))
    while(n!=1):
        if n%2:
            n=(3*n) + 1
        else:
            n=n/2
        i=i+1
    return i
        