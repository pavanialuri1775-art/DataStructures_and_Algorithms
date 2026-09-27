#109.24. Reverse a list without reverse().
ls=[1,2,3,4,5,6]
new_ls=[]
for i in range(len(ls)-1,-1,-1):
    new_ls.append(ls[i])
print(new_ls)