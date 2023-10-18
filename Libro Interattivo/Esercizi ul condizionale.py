#1
# def value(n):
#     if (n>=90):
#         return "A"
#     elif (n>=80):
#         return "B"
#     elif (n>=70):
#         return"C"
#     elif(n>=60):
#         return "D"
#     else:
#         return "F"
    
    
# def main():
#     n=float(input("Numeric Vote: "))
#     print("Vote: ",value(n))
    
#2
# def is_even(n):
#     return not(bool(n%2))

# def is_odd(n):
#     return not(is_even(n))
# def main():
#     x=float(input("insert number: "))
#     print ("is_even:",is_even(x), "\t is odd: ", is_odd(x))   
    

def isLepYear(y):
    if( (y%100 == 0)):
        if(y%400 == 0) :
            return True
        else:
            return False
    elif not(y%4):
        return True
    else:
        return False

def main():
    y=int(input("Year:  "))
    if(isLepYear(y)):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()