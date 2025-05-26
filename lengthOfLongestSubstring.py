def lengthOfLongestSubstring(s: str) -> int:
        last_seen = {}
        left = 0
        max_length = 0
        window = 0
        for right in range(len(s)):
            current_letter = s[right]
            if s[right] in last_seen and left < last_seen[s[right]] + 1:
                left = last_seen[s[right]] + 1
                last_seen[s[right]] = right
                
            else:
                last_seen[s[right]] = right
            window = right - left + 1
             
            max_length = max(max_length, window)
            
        return max_length
  
if __name__ == "__main__":
    s = input("Enter your string: ")
    print(f"Length of the longest substring without repeating characters: {lengthOfLongestSubstring(s)}")
