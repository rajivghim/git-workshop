def is_palindrome(s):
    # Convert to lowercase and remove spaces for a more robust check
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("Racecar"))  # Output: True
