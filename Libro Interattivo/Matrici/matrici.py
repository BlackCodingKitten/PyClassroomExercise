def diag_List(M=[], i =0, l=[]):
    if i>=len(M):
        return l
    else: 
        l.append(M[i][i])
        return diag_List(M,i+1,l)

def diag_Dic(M={},i=0, l=[]):
    v=M.get((i,i),None)
    if v == None:
        return l
    else:
        l.append(v)
        return diag_Dic(M,i+1,l)
        
def simmetric_L(M, i=0, j=1):
    # f = True
    # for i in range(len(M)):
    #     for j in range(len(M)):
    #         f = f and M[i][j] == M[j][i]
    # return f
    
    if i<len(M):
        if i<len(M)
            
         
        


def main():
    M= {
    (0, 0): 56, (0, 1): 0, (0, 2): 0, (0, 3): 0,
    (1, 0): 0, (1, 1): 56, (1, 2): 0, (1, 3): 0,
    (2, 0): 0, (2, 1): 0, (2, 2): 56, (2, 3): 0,
    (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 56,
    }    
    Ms = {
    (0, 0): 7, (0, 1): 2, (0, 2): 3, (0, 3): 4,
    (1, 0): 2, (1, 1): 5, (1, 2): 6, (1, 3): 7,
    (2, 0): 3, (2, 1): 6, (2, 2): 8, (2, 3): 9,
    (3, 0): 4, (3, 1): 7, (3, 2): 9, (3, 3): 10,
    }
    m = [
    [56, 0, 0, 0],
    [0, 56, 0, 0],
    [0, 0, 56, 0],
    [0, 0, 0, 56]
    ]
    ms = [
    [1, 2, 3, 4],
    [2, 5, 6, 7],
    [3, 6, 8, 9],
    [4, 7, 9, 10]
    ]

    # print(diag_List(ms))
    # print(diag_Dic(Ms))
    print(simmetric_L(ms))
    
main()