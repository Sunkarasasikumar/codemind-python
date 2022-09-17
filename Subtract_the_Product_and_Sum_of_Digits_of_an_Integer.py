n=int(input())
sum,pro=0,1
while n:
    r=n%10
    sum+=r
    pro*=r
    n=n//10
print(pro-sum)