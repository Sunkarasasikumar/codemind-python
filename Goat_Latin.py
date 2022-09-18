s=input()
l=list(s.split())
vowels=['a','e','i','o','u']
j=1
for i in l:
    if i[0]=='a' or i[0]=='e' or i[0]=='i'or i[0]=='o' or i[0]=='u':
        i=i+'ma'+j*'a'
    else:
        i=i[1:]+i[0]+'ma'+j*'a'
    j+=1
    print(i,end=" ")