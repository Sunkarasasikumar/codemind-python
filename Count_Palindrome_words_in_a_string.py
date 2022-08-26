def is_palin(i):
    if i==i[::-1]:
        return True
    return False
n=input()
n=n.lower()
l=n.split()
count=0
for i in l:
    if is_palin(i):
        count+=1
print(count)