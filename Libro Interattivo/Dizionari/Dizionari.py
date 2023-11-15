import random

def es1(string):
    d = { }
    for i in string.lower():
        if ord(i)>=97 and ord(i)<=122:
            if i in d:
                d[i]= int(d.get(i) + 1)
            else:
                d[i] = 1
    
    for k in sorted(d):
        print(k, ",", d[k])
    print("$")

def pirate(string):
    
    translations = {
    'sir': 'matey',
    'hotel': 'fleabag inn',
    'student': 'swabbie',
    'boy': 'matey',
    'madam': 'proud beauty',
    'professor': 'foul blaggart',
    'restaurant': 'galley',
    'your': 'yer',
    'excuse': 'arr',
    'students': 'swabbies',
    'are': 'be',
    'lawyer': 'foul blaggart',
    'the': 'th’',
    'restroom': 'head',
    'my': 'me',
    'hello': 'avast',
    'is': 'be',
    'man': 'matey',
    }
    
    translation = " "
    for word in (string.lower()).split():
        if word in translations:
            translation = translation + str(translations.get(word,word))
        else: 
            translation = translation + word
        translation +=" "
    return translation

def sommaMat (n,m):
    d_matrix = {}
    l_matrix = []
    
    for i in range(n):
        temp = []
        for j in range(m):
            x=random.randint(0,100)
            temp.append(x)
            d_matrix[(i,j)]=x
        l_matrix.append(temp)
    # print(l_matrix, d_matrix)
    
    l_sum = 0
    d_sum = 0
    for i in range(n):
        for j in range (m):
            l_sum += l_matrix[i][j]
            
    for (k,v) in d_matrix.items():
        d_sum += v
    
    return l_sum,d_sum
            
    
    




def main():
    
    # es1("ThiS is String with Upper and lower case Letters.")
    # print(pirate("hello my name is michela"))
    print(sommaMat(4,4))

main()