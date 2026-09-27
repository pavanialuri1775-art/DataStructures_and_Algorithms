a=[1,2,3,4,5,6,7]
b=[5,2,3,9,15]
ls=[]
for ch in a:
    if ch in b:
        ls.append(ch)
print(ls)