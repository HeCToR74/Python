def palindrome(s):
    return s == s[::-1]


# Tests
# print(palindrome('abccba'))  # True
# print(palindrome('Abccba'))  # False
# print(palindrome('abcc ba'))  # False
# print(palindrome('abcca'))  # False
# print(palindrome('ab c ba'))  # True
