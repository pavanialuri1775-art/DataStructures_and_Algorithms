#95.10. Find the sum of digits of a number.
n=input("enter a number:")
total=0
for num in n:
    total+=int(num)
print(total)