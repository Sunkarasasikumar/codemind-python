n=input()
l=n.split()
max=0
for i in l:
    if max<len(i):
        max=len(i)
print(max)