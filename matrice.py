a=[[2,11,54,3,1],
[34,6,55,9,22],
[1,2,3,4,5],
[9,7,6,45,0],
[12,23,34,45,56]]
for i in a:
    print("suma randului",i+1,"este",sum(i))

for i in range(len(a)):
    col=[]
    for rind in a:
        col.append(rind[i])
    print("suma coloanei",i+1,"este",sum(col))

d_principala=[]
d_secundara=[]
for i in range(len(a)):
    for j in range(len(a[0])):
        if i==j:
            d_principala.append(a[i][j])
        if i+j==(len(a)-1):
            d_secundara.append(a[j][i])

print("Diagonala principala-",d_principala)
print("Diagonala secundara-",d_secundara)