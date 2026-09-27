#104.19. Count words in a sentence.
s=input("enter a sentence:")
s=s.split()
count=0
for ch in s:
    count+=1
print(count)