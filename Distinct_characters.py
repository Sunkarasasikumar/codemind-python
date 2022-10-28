s=input()
l=s.lower()
a=[]
for i in l:
    if l.count(i)==1 and i!=' ':
        if i in s:
            a.append(i)
        else:
            a.append(i.upper())
a.sort()
print(''.join(a))
