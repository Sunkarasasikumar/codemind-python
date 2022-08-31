n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    if i!=n-1:
        l[i]=max(list(l[j] for j in range(i+1,n)))
        print(l[i],end=" ")
    else:
        l[i]=-1
        print(l[i])