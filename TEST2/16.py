# Find the second-largest number.
arr=[1,2,3,4,5,6,7]
fst_lar=float('-inf')
sec_lar=float('-inf')
for num in arr:
    if num>fst_lar:
        sec_lar=fst_lar
        fst_lar=num
    elif num>sec_lar and num!=fst_lar:
        sec_lar=num
print(sec_lar)
    