def print_st():
    f = open("./st_data.txt", "r")
    for i in f: 
        t = i.split()
        if len(t)>7:
            print(t[0])
    f.close()
    return

def avg():
    f = open("./st_data.txt", "r")
    for i in f: 
        t = i.split()
        a=0
        for i in t[1:]:
            a +=int(i)
        print(t[0],": ",round(a/len(t[1:]),2))
    f.close()
    return

def min_max():
    f = open("./st_data.txt", "r")
    for i in f: 
        t = i.split()
        voti = []
        for k in t[1:]:
            voti.append(int(k))
        voti.sort()
        # if t[0]=="sue":
        #     print(voti)
        print(t[0], "\tmax: ", voti[-1], " min: ", voti[0] )
    f.close()
    
def labdata():
    f = ("./lab_data.txt", "r")
    line = f.readline()
    while line:   
    
def main():
    # print_st()
    # avg()
    # min_max()


main()