n=input()
l=n.split()
x,y=[],[]
for i in l:
    max=-99
    min=9999
    for j in i:
        if ord(j)>max:
            max=ord(j)
        if min>ord(j):
            min=ord(j)
    print(abs(min-max),end=" ")