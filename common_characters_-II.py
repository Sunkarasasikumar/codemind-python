A=set(input().lower())
B=set(input().lower())
L=A.intersection(B)
count=0
for i in L:
    if i.isalpha():
        count+=1
print(count)