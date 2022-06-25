# Runtime: 110 ms, faster than 11.35% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14.3 MB, less than 99.15% of Python3 online submissions for Valid Palindrome.

s = "A man, a plan, a canal: Panama"
s = "race a car"
s = " "
s = "0P"

def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and s[l].isalnum() == False: 
            l += 1
        while l < r and s[r].isalnum() == False: 
            r -= 1
        if s[l].lower() != s[r].lower(): 
            return False
        l += 1
        r -= 1
    return True

res = isPalindrome(s)
print(res)