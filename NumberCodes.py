# NumberCodes.py

num = int(input("Enter a number: "))

reverse = int(str(num)[::-1])

print("Original Number:", num)
print("Reversed Number:", reverse)

if num == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
