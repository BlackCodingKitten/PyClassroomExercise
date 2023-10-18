def isEqual(a,b):
    return a==b

def main():
    x=float(input("valore 1:"))
    y=float(input("valore 2:"))
    
    print("pass" if isEqual(x,y) else "not pass")

if __name__ == "__main__":
    main()