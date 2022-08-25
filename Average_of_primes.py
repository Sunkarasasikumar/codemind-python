def is_prime(p):
    if p<2:
        return False
    for i in range(2,(p+2)//2):
        if p%i==0:
            return False
    return True
N=int(input())
l=list(map(int,input().split()))
count=0
sum=0
for i in range(len(l)):
    if is_prime(l[i]):
        count+=l[i]
        sum+=1
print("{:.2f}".format(count/sum))