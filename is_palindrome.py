def is_palindrome(string):
    return string == string[::-1]


# Driver code
s = "malayalam"
ans = is_palindrome(s)

if ans:
    print("Yes")
else:
    print("No")