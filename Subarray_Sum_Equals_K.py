n,k=map(int,input().split())
l=list(map(int,input().split()))
count=0
for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=l[j]
        if sum==k:
            count+=1
            break
        elif sum<k:
            continue
        else:
            break
print(count)
        