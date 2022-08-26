def sum_digit(n):
    if len(str(n))==1:
        return n
    else:
        s=0
        n=str(n)
        #print(n)
        for i in n:
            s+=int(i)
        return s
n=int(input())
l=list(map(int,input().split()))
Sum=0
for i in l:
    Sum+=sum_digit(i)
print(Sum)
    