s=input()
#print(s)
l=list(s)
#print(l)
for i in l:
    if i=='.':
        i='[.]'
    print(i,end='')
