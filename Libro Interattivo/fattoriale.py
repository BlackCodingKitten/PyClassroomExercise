# n = int(input("Fattoriale di : "))
# fat = 1
# for i in range(n):
#     fat = fat * (n+1)
# print(f"Il fattoriale e' {fat}")

n = int(input("Inserisci n : "))
k = int(input("Inserisci k : "))
if(n<k):
    print ("risultato 0")
    exit(0)
kfat = 1
nfat = 1
nkfat = 1
for i in range(n):
    nfat = nfat* (i+1)
for i in range(k):
    kfat = nfat* (i+1)
for i in range(n-k):
    nkfat = nkfat* (i+1)

cBin = nfat/(kfat * nkfat)
print (f"risulato {cBin}")