n=int(input())
l=list(map(int,input().split()))
count=sum=0 
for i in l:
    if i==1:
        count+=1
    else:
        if count>sum:
            sum=count
        count=0
print(count if count>sum else sum)