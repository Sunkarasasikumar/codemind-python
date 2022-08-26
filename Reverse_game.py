def sum_digit(n):
    if len(str(n))==1:
        return n
    else:
        n=str(n)
        rev=0
        for i in range(len(n)):
            rev=rev*10+int(n[len(n)-i-1])
        return rev
n=int(input())
l=list(map(int,input().split()))
lis=[]
for i in l:
   lis.append(sum_digit(i))
for i in lis:
    print(i,end=" ")
    