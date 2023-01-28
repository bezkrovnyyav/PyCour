"""
Check if the string is Symmetrical or Palindrome
Given a string. The task is to check if the string is symmetrical or palindrome. A string is said to be symmetrical
if both the halves of the string are the same and a string is said to be a palindrome string if one half of the string
is the reverse of the other half or if a string appears same when read forward or backward.
Input: khokho
Output:
The entered string is symmetrical
The entered string is not palindrome
Input: amaama
Output:
The entered string is symmetrical
The entered string is palindrome
"""
def check_semmetrical(word):
    length_word = len(word)

    if length_word % 2 == 0:
        half_word = int(length_word / 2)
        first_half_word = word[:half_word]
        first_half_word = word[half_word:]
        if first_half_word == first_half_word:
            return "Symmetrical"
        else:
            return "Not symmetrical"
    else:
        return "Not symmetrical" 

def check_palindrome(word):
    result = check_semmetrical(word)     

    if word == word[::-1]:
        return ("Palindrome", result)
    else:
        return ("Not palindrome", result)
