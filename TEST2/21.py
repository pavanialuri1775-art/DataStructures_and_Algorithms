#112 Move all zeros to the end.
ls=[1,2,0,3,0,4,0,5,0]
num_ls=[]
zero_ls=[]
for ch in ls:
    if ch!=0:
        num_ls.append(ch)
    else:
        zero_ls.append(ch)
num_ls.extend(zero_ls)
print(num_ls)