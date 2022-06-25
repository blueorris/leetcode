# Runtime: 83 ms, faster than 31.71% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 15.3 MB, less than 26.36% of Python3 online submissions for Valid Palindrome.
# Warning: check both alphabet & number: use isalnum() function

s = "A man, a plan, a canal: Panama"

def isPalindrome(s) -> bool:
    str_lower = s.lower()
    str_letter = "".join([i for i in str_lower if i.isalnum() == True])
    reverse_letter = "".join([str_letter[i] for i in range(len(str_letter)-1, -1, -1)])
    if str_letter == reverse_letter:
        return True
    else:
        return False

res = isPalindrome(s)
print(res)