def is_prime(p):
    if p<2:
        return False
    for i in range(2,(p+2)//2):
        if p%i==0:
            return False
    return True
N=int(input())
l=list(map(int,input().split()))
maxi=max(l)
mini=min(l)
maxi=l.index(maxi)
mini=l.index(mini)
count=0
sum=0
if mini>maxi:
    for i in range(mini,maxi-1,-1):
        if is_prime(l[i]):
            count+=1
else: 
    for i in range(mini,maxi+1):
        if is_prime(l[i]):
            count+=1
print(count if count >0 else "-1")
