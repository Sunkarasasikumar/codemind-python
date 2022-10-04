l=int(input())
r=int(input())
count=0
for i in range(l,r+1):
    sum=0
    for j in range(i,r+1):
        sum+=j
        if sum%2==1:
            count+=1
print(count)
        