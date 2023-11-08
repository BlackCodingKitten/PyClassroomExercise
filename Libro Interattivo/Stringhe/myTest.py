def testEqual(x,y):
    #esegue il controllo di tipo
    if(type(x) == type(y)):
        if(type(x) == float and type(y) == float):
            #Confronto più acurato per i float
            if(abs(x-y) < (10**-9)):
                return "#Pass"
            else:
                return "#Expected "+ str(x) + " got "+ str(y)
        elif(x==y):
            return "#Pass"
        else:
            return "#Expected "+ str(x) + " got "+ str(y)
    elif ((type(x) == float) or (type(y) == float)) and ((type(x) == int) or (type(y) == int)):
        if(x==y):
            return "#Pass"
        else:
            return "#Expected "+ str(x) + " got "+ str(y)
    else:
        return"#Fail expected type "+ str(type(x)) +" got type "+ str(type(y)) 
