n=input()
l=n.split()
for i in range(len(l)):
    if i%2==0:
        l[i]=l[i][::-1]
r=" ".join(l)
print(r)