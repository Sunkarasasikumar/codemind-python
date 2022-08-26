n=input()
l=n.split()
mini=9999999
for i in l:
    if mini>len(i):
        mini=len(i)
print(mini)