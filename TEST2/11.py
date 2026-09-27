#97.12. Check whether a string is a palindrome.
s=input("enter:")
if s==s[::-1]:
    print("palindrome")
else:
    print("not a palindrome")