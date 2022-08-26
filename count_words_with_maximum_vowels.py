n=input()
n=n.lower()
l=n.split()
vowel=['a','e','i','o','u']
mcount=[]
for i in l:
    count=0
    for j in i:
        if j in vowel:
            count+=1
    mcount.append(count)
mcount.sort()
print(mcount.count(mcount[-1]))

    