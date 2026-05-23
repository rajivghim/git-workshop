def is_palindrome(s):
    # Convert to lowercase and remove spaces for a more robust check
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Ask the user to enter a word
word = input("Enter a word to check if it's a palindrome: ")
result = is_palindrome(word)
print(f"'{word}' is a palindrome: {result}")
