#Count vowels and consonants.
s=input("enter a name")
vowels="AEIOUaeiou"
v_count=0
c_count=0
for ch in s:
    if ch in vowels:
        v_count+=1
    else:
        c_count+=1
print("vowel_count:",v_count)
print("consonant_count",c_count)
        
    