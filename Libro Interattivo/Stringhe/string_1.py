import myTest
from myTest import testEqual 

def inttoString(x):
    x = str(x)
    return len(x)

def eCounter(text):
   c = len(text) 
   perc = (text.count("e")/len(text)) * 100
   print("Ci sono ", c, " catatteri di cui le 'e' sono ",text.count("e")," ossia il ", round(perc,2), "'%' del totale")

def reverse (astring):
    acc= ""
    for i in range(len(astring)):
        index = (i+1)*-1
        acc=acc+astring[index]
    return acc 

def mirror (astring):
    return astring + reverse(astring)   

def remove_letter(letter, astring):
    acc=""
    for e in astring:
        if letter == e:
            continue
        else:
            acc=acc+e
    return acc

def is_palindrome(astring):
    return astring.lower() == reverse(astring).lower()


def count(substr,theStr):
    if len(theStr)<len(substr):
        return 0
    elif theStr[:len(substr)] == substr:
        return 1 + count(substr,theStr[1:])
    else:
        return count(substr, theStr[1:])
    
# def removeDups(astring):
#     if len(astring)==0:
#         return ""
#     elif astring[-1] in astring[0 : len(astring)-2]: 
#         return ""
#     else:
#         return removeDups(astring[0 : len(astring)-2]) + astring[-1]
            
# def removeDups(string):
#     acc = ""
#     for i in string:
#         if i not in acc: 
#             acc += i
#     return acc

# def fun():
#     a=[14,13,11]
#     b=a[:]
#     c=a[:]
#     n=[]
#     n.append(b)
#     n.append(b)
    
#     print( b is c, n[0] is n[1])
    
def main():
    # text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    # print(inttoString(5673))
    # print(testEqual(reverse("happy"), "yppah"))
    # print(testEqual(reverse("Python"), "nohtyP"))
    # print(testEqual(reverse(""), ""))
    # print(testEqual(mirror('good'), 'gooddoog'))
    # print(testEqual(mirror('Python'), 'PythonnohtyP'))
    # print(testEqual(mirror(''), ''))
    # print(testEqual(mirror('a'), 'aa'))
    # print(remove_letter("barabagianni", "a"))
    # print(testEqual(remove_letter('a', 'apple'), 'pple'))
    # print(testEqual(remove_letter('a', 'banana'), 'bnn'))
    # print(testEqual(remove_letter('z', 'banana'), 'banana'))
    # print(testEqual(is_palindrome('abba'), True))
    # print(testEqual(is_palindrome('abab'), False))
    # print(testEqual(is_palindrome('straw warts'), True))
    # print(testEqual(is_palindrome('a'), True))
    # print(testEqual(is_palindrome(''), True))
    # print(testEqual(count('is', 'Mississippi'), 2))
    # print(testEqual(count('an', 'banana'), 2))
    # print(testEqual(count('ana', 'banana'), 2))
    # print(testEqual(count('nana', 'banana'), 1))
    # print(testEqual(count('nanan', 'banana'), 0))
    # print(testEqual(count('aaa', 'aaaaaa'), 4))
    # print(removeDups("mississipi"))
    fun()
    # eCounter(text)


    
main()