n1=input()
n2=input()
n1,n2=n1.lower(),n2.lower()
l1=n1.split()
l2=n2.split()
count=0
for i in l1:
    if i in l2:
        count+=1
print(count)