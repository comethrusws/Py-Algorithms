# Check if a given string is a palindrome.

#hmm, so basic idea here would be 2 change the string first to lowercase, then check

def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]

text = "A man a plan a canal Panama"
print(f'Is "{text}" a palindrome? {is_palindrome(text)}')