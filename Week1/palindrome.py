def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

print(is_palindrome('noon'))
print(is_palindrome('racecar'))
print(is_palindrome('dented'))
print(is_palindrome('r'))
print(is_palindrome('ro'))
