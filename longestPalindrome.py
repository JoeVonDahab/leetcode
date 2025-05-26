class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0 
        max_lenght = 0
        longest = ""
        
        for left in range(len(s)):
            for right in range(left, len(s)):
                substring= s[left:right+1]
                if substring == substring[::-1] and len(substring) > max_lenght:
                    max_lenght = len(substring)
                    longest = substring
            
        return longest
