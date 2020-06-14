L=[]
J=[]
N=int(input("Enter Your fav Number"))
for i in range(N):
    X=int(input("Enter the elements  to the list"))
    L.append(X)
print(L)
for i in L:
    if i>0:
        J.append(i)
print(J)
