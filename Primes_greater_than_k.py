def is_prime(p):
    if p<2:
        return False
    for i in range(2,(p+2)//2):
        if p%i==0:
            return False
    return True
N=int(input())
l=list(map(int,input().split()))
k=int(input())
count=0
for i in range(len(l)):
    if is_prime(l[i]) and l[i]>=k:
        count+=1
print(count)