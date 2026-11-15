class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = ''
        for i in s:
            if i.isalnum():
                b += i.lower()
        
        start = 0
        end = len(b) - 1

        palindrome = True

        while start < end:
            if b[start] == b[end]:
                start += 1
                end -=1
                palindrome = True
            else:
                palindrome = False
                break
    
        return palindrome