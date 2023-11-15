def stampaPari(s, i=0):
    if len(s) <= 0:
        return ""
    else:
        # print(s[0], i)
        if  (i%2) or (ord(s[0]) >=32 and ord(s[0])<=64)  :
            # è una simbolo di punteggiatura o sono su indice dispari
            return stampaPari(s[1:], i+1)
        else:
            return s[0] + stampaPari(s[1:], i+1)
    
def sommaLunghezze (somma=0):
    s = list(input("inserisci una stringa, [] per temrinare: "))
    if s==[]:
        return somma
    # >=65 ,>=90<
    if ord(s[0]) >= 65 and ord(s[0]) <=90:
        return sommaLunghezze(somma + len(s))
    else:
        return sommaLunghezze(somma)

def maxListe(l, max=0, i=-1):
    if l==[]:
        return (max,i)
    
    if l[0]>max :
        return maxListe(l[1:], l[0], i+1)
    else:
        return maxListe(l[1:], max, i+1)

def azzeraCoppie(v , value =0, i=0):
    if i >= len(v):
        return v
    else:
        if(value !=0 and value==v[i]):
            v[i]=0
        else:
            value = v[i]
            if  (i+1)<len(v) and value == v[i+1]:
                v[i]=0
        return azzeraCoppie(v, value, i+1)
            

def inserisciCatalogo(catalogo,autore,titolo,isbn,anno):
    if not(type(autore)==str and type(titolo)==str and type(isbn)==int and type(anno)==int):
        print("Errore di tipo")
        return False
    elif catalogo.get(isbn) != None:
        print("Elemento già presente")
        return False
    else:
        catalogo[isbn]=(autore, titolo, isbn, anno)
        return True

def stampaCatalogo(catalogo, p=0):
    if p<0 or p>3:
        return "Errore"
    for (aut,tit,isbn,anno) in sorted(catalogo.values(), key=lambda x:x[p]):
        print(aut," ",tit," ",isbn," ",anno)   
    
def main():
    # print(stampaPari("il cane:ciao",))
    # print(maxListe([1,2,3]))
    # print(sommaLunghezze())
    # print(azzeraCoppie([1,2,3,3,3,3,4,5,5,7]))
    catalogo = {
    123456781: ('John Smith', 'Programming Basics', 123456781, 2020),
    234567892: ('Jane Doe', 'Data Science Essentials', 234567892, 2019),
    345678903: ('Bob Johnson', 'Web Development Guide', 345678903, 2021),
    456789014: ('Alice Brown', 'Machine Learning Fundamentals', 456789014, 2018),
    567890125: ('Charlie Wilson', 'Networking 101', 567890125, 2022),
    678901236: ('Eva Miller', 'Python for Beginners', 678901236, 2017),
    789012347: ('David White', 'Artificial Intelligence Insights', 789012347, 2023),
    890123458: ('Grace Davis', 'Cybersecurity Handbook', 890123458, 2016),
    901234569: ('Frank Taylor', 'Software Engineering Principles', 901234569, 2024),
    912345670: ('Sophie Reed', 'Database Management', 912345670, 2015),
}

    # print(inserisciCatalogo(c, "Gatto", 237487982, 0.5,2023))
    p = int(input("Inserisci 0 per oridnare per autore, 1 per titolo, 2 per isbn, 3 per anno: "))
    stampaCatalogo(catalogo,p)
    
main()