A=set(input().lower())
B=set(input().lower())
R=[]
L=A.intersection(B)
for i in A:
    if i in L:
        continue
    else:
        R.append(i)
for i in B:
    if i in L:
        continue
    else:
        R.append(i)
R.sort()
count=0
for i in R:
    if i.isalpha():
        count+=1
print(count)
