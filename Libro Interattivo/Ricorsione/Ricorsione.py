def rec_sum(n):
    if n == 0: 
        return 0
    return n + rec_sum(n-1)

def rec_pow(e,b):
    if e==0: 
        return 1
    return b * rec_pow(e-1,b)

def rec_double (prec = 0, flag=True):
    n = 0
    if (n=int(input("inserisci un valore")) == 0):
        return flag
    else:  
        if prec<0:
            return(n,)
        else: 
            


def main():
    if rec_double():
        print(True)
    else:
        print(False)
    
main()