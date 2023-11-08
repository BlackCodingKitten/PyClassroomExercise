def somma(n):
    if(n==0):
        return 0
    else:
        return n+somma(n-1)
    
def pow(b,e):
    if e == 0 :
        return 1
    else:
        return b*pow(b,e-1)
    
def verify(prec=-1, flag = True):
    curr = int(input("Inserisci un valore o 0 per teminare "))
    if (prec == -1) or (curr == (2*prec)):       
        return verify(curr,flag)
    elif (curr==0):
        return flag   
    else:
        return verify(curr,False)
    
def catalan(n, n1=1):
    print(int(n1))
    if(n==0):
        return
    else:
        a = 4*n1
        a = a+2
        b= n1 + 2
        n1 = (a/b) * n1
        catalan(n-1, int(n1))

def inverse():
    x=int(input("Inserisci un intero "))
    if(x==0):
        return
    else:
        inverse()
        print(x)

def hanoi(n, A, B, C):
    if(n==1):
        print("Move: ", A, " in ", B)
        return
    else:
        hanoi(n-1,A,C,B)
        print("Move: ", A, " in ", B)
        hanoi(n-1,C,B,A)
    
    
    
def main():
    # print(somma(6))
    # print(pow(2,3))
    # print(verify())
    # catalan(5)
    # inverse()
    hanoi(3, "P1", "P2", "P3")
    
    
    
    
main()