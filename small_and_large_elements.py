n=input()
l=n.split()
min=l[0][0]
for i in l[0]:
    if ord(min)>ord(i):
        min=i
print(min,end=" ")
max=l[-1][0]
for i in l[-1]:
    if ord(i)>ord(max):
        max=i
print(max)
    