# Runtime: 91 ms, faster than 22.95% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14.5 MB, less than 57.23% of Python3 online submissions for Valid Palindrome.

s = "A man, a plan, a canal: Panama"

def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not alphanum(s[l]): 
            l += 1
        while l < r and not alphanum(s[r]): 
            r -= 1
        if s[l].lower() != s[r].lower(): 
            return False
        l += 1
        r -= 1
    return True

# Could write own alpha-numeric function
def alphanum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))

res = isPalindrome(s)
print(res)