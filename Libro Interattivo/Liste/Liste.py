import myTest
from myTest import testEqual

import random

def average(list):
    acc=0
    for i in list:
        acc+=i
    return acc/len(list)
    
def max(list):
    list.sort()
    return list.pop()

def sum_of_square(list):
    x=0
    for i in [pow(item,2) for item in list]:
        x+=i
    return x

def odd_counter(list):
    return len([1 for item in list if (item%2)])

def even_sum(list):
    return sum([item for item in list if not(item%2)])

def negative_sum(list):
    return sum([item for item in list if item<0])

def five_char_counter(list):
    if list==[]:
        return 0
    if len(list[0]) ==5:
        return 1+five_char_counter(list[1:])
    else:
        return five_char_counter(list[1:])

def es8(list):
    if list == [] or not(list[0]%2):
        return 0
    return list[0]+es8(list[1:])

def world_counter(list):
    if list == [] or list[0]=="sam":
        return 0
    return 1+ world_counter(list[1:])

def myCount(list,elem):
    return len([i for i in list if i == elem])

def myIn(list,elem):
    for i in list:
        if i==elem:
            return True
    return False

     
def myInsert(list,index,item):
    l = list[0:(index-1)]
    l.append(item)
    l.append(list[index:])
    return l
    
    
def myIndex(list,elem):
    for i in range(len(list)):
        if list[i]==elem:
            return i
    return-1
    
def myReverse(list):
    l=[]
    for i in range(len(list)):
        l.append(list.pop())
    return l
    
def replace(string, old, new):
    l = string.split(old)
    return new.join(l)
        
def k_list ():
    k=int(input("K: "))
    A =[]
    for i in range(k):
        A.append(int(input("Numero: " )))
    B = A[:]
    return (A,B)

def condition ():
    k=int(input("K: "))
    A =[]
    if(k%2):
        return "Error k deve essere pari"
    for i in range(k):
        A.append(int(input("Numero: " )))
    X=int(input("X: "))
    som=0
    for i in range(0,k,+2):
        som+=A[i]
    if X<som:
        return "Condizione non verificata"
    return "Condizione verificata"

def sommaContigua():
    k=int(input("K: "))
    A =[]
    if(k%2):
        return "Error k deve essere pari"
    for i in range(k):
        A.append(int(input("Numero: " )))
    X=int(input("X: "))
    for i in range(0,k,+2):
        if(A[i]+A[i+1] != X):
            return "Condizione non verificata"
    return "Condizione verificata"

def XprecY():
    k=int(input("K: "))
    A =[]
    for i in range(k):
        A.append(int(input("Numero: " )))
    X=int(input("X: "))
    Y=int(input("Y: "))
    for i in range(k-1):
        if((A[i]==X) and (A[i+1]!=Y)):
            return "Condizione non verificata"
    return "Consizione verificata"
    
def even_copy(A):
    return[i for i in A if not(i%2)]  

def concatInC(A,B):
    C= A[:] + B[:]
    return C

def es18(A,B):
    return A + B[:]
    
def union(A,B):
    C=A[:]
    for i in B:
        if i not in C:
            C.append(i)
    return C

def intersection(A,B):
    C = []

    if len(A)>=len(B):
        for i in range(len(B)):
            if ((B[i]) in A):
                C.append(B[i])
    else:
        for i in range(len(A)):
            if ((A[i]) in B):
                C.append(A[i])
    return C
    
# def intersezioneOrdinata (A,B):
#     i=0 
#     j=0
#     C=[]        
#     while (i<len(A))and (j<len(B)):
#         print("i: ", i, "j: ", j ,"C: ", C)
#         if A[i]==B[j]:
#             C.append(A[i])
#             i+=1
#             j+=1
#         else:
#             while  (j<len(B)) and (A[i]>B[j]):
#                 j+=1
                
#             while (i<len(A)) and  (A[i]<B[j]):
#                 i+=1
#     return C

def intersezioneOrdinata(A, B):
    i = 0
    j = 0
    C = []

    while i < len(A) and j < len(B):
        print("i: ", i, "j: ", j, "C: ", C)
        if A[i] == B[j]:
            C.append(A[i])
            i += 1
            j += 1
        elif A[i] > B[j]:
            j += 1     
        else:
            i += 1

    return C
            
        
# Controllo dell'uso delle parentesi:
def verifica_parentesi(stringa):
    # stack = []
    # parentesi_aperte = {'{', '(', '['}
    # parentesi_chiuse = {'}', ')', ']'}
    # mappa_parentesi = {')': '(', '}': '{', ']': '['}

    # for c in stringa:
    #     if c in parentesi_aperte:
    #         stack.append(c)
    #     elif c in parentesi_chiuse:
    #         if not stack or stack.pop() != mappa_parentesi[c]:
    #             return False

    # return not stack
    
    stack = []
    parentesi_aperte = {'{', '(', '['}
    parentesi_chiuse = {'}', ')', ']'}

    for c in stringa:
        if c in parentesi_aperte:
            stack.append(c)
        elif c in parentesi_chiuse:
            if not stack or (c == '}' and stack[-1] != '{') or (c == ')' and stack[-1] != '(') or (c == ']' and stack[-1] != '['):
                return False
            stack.pop()

    return not stack



  
        
        

                   
def main():
    # list=[]
    # for i in range(100):
    #     list.append(random.randint(0,100))
    # print(average(list))
    # print(max(list))
    
    # list = [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2]
    # print(sum_of_square(list))
    # print(odd_counter(list))
    # print (even_sum(list))
    # print(negative_sum(list))
    
    # list = ["gatto", "cane", "aaaaa","sam", "aaaaa", "aaaaa","aaaaa","aaaaa","aaaaa","aaaaa", "a", "aa"]
    # print(five_char_counter(list))
    
    # list = [1,1,1,1,1,1,1,6,45]
    # print(es8(l))
    # print(world_counter(list))
    
    # print(myReverse(list))
    # print(myIndex(list,"sam"))
    # print(myIn(list,"banana"))
    # print(myCount(list, "aaaaa"))
    # print(testEqual(replace('Mississippi', 'i', 'I'), 'MIssIssIppI'))
    # s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
    # print(testEqual(replace(s, 'om', 'am'),
    #     'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!'))

    # print(testEqual(replace(s, 'o', 'a'),
    #     'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!'))
    # print(k_list())
    # print(condition())
    # print(sommaContigua())
    # print(XprecY())
    
    # list=[1,2,3,4,5,6,7,8,9]
    # list2=[3,3,3,3,3,3,5]
    # print(even_copy(list))
    # print(concatInC(list,list2))
    # C=es18(list,list2)
    # print(C)
    # list2=[3,3,3,3,3,3,5,89]
    # print(C)
    
    # A=[1,2,3,4,5,4,3,5,89,56,112]
    # B=[11,12,13,5,3,2,56,89]
    
    # print("Unione: ",union(A,B))
    # print("Intesection: ", intersection(A,B))
    # A=[]
    # B=[]
    # for i in range(10):
    #     A.append(random.randint(0,100))
    # B=A[1:9]+[4,6,7,23,56,95]
    # print(A,B)
    # A.sort()
    # B.sort()
    # A
    # print(A,B)
    
    # print(intersezioneOrdinata(A,B))
    
    input_utente = input("Inserisci una stringa: ")
    if verifica_parentesi(input_utente):
        print("La sequenza è corretta.")
    else:
        print("La sequenza non è corretta.")
        
main()

