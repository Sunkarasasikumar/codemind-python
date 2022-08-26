s=input()
l=s.split()
n=l[-1]
min=9999999999
min_word=""
for i in n:
     if min>ord(i):
         min=ord(i)
         min_word=i
if min_word.lower() in n:
    print(min_word.lower())
else:
    print(min_word)
