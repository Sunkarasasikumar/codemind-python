def Exchange(l,n):
    t=[0 for i in range(n)]
    k=0
    for i in range(n-1,(n-1)//2,-1):
        t[k]=l[i]
        k+=1
    #print(t)
    for i in range(0,n//2):
        t[k]=l[i]
        k+=1
    #print(t)
    return t
n=int(input())
l=list(map(int,input().split()))
l=Exchange(l,n)
#print(l)
for i in l:
    print(i,end=' ')
        
        