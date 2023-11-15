
def main():
    fileref = open ("./file.txt", "r")
    # fileref2 = open ("./file.txt", "r")
    # fileref3 = fileref
    # print(fileref)
    # print(fileref is fileref2)
    # print(fileref3 is fileref)
    # fileref3.close()
    # flag = fileref2.closed
    # print(flag)
    for i in fileref:
        v = i[:(len(i)-2)].split()
        print("Nome Cognome: ", v[0]," ",v[1], "\t\t\t Rate: ", v[-2])
        
    fileref.close()
    # fileref2.close()
    
main()