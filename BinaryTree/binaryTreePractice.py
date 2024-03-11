s="babad"
seen={}
l=0
length=0

stack=[s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]

for i in stack:
    if i==i[::-1]:
