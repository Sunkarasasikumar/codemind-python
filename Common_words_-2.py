S1=input()
S2=input()
a=S1.split()
b=S2.split()
for i in a:
    if a.count(i)>=2:
        for j in range(a.count(i)):
            a.remove(i)
for i in b:
    if b.count(i)>=2:
        for j in range(b.count(i)):
            b.remove(i)
a,b=set(a),set(b)
print(len(a.intersection(b)))

