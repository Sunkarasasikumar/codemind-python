s1=(input().lower()).split()
#print(s1)
s2=(input().lower()).split()
#print(s2)
l=[]
for i in s2:
    if i in s1:
        print(i,end=" ")