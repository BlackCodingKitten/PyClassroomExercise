

def min (min, v):
    if(min<v):
        return min
    else: 
        return v


def max (max, v):
    if(max>v):
        return max
    else: 
        return v

def sum(s, v):
    return s+v


def main():
    m =0
    M=0
    S =0

    for i in range (10):
        print("Numero", i+1, "esimo")
        v = float(input())
        m = min(m, v)
        M = max(M, v)
        S = sum(S, v)

    print ("Massimo", M, "Minimo", m, "Somma", S)
   

if __name__ == "__main__":
    main()