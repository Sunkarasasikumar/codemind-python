n=input()
min=n[0]
max=n[0]
for i in n:
    if i.isalnum():
        if min>i:
            min=i
        if max<i:
            max=i
    else:
        continue
print(min,n.count(min),max,n.count(max))