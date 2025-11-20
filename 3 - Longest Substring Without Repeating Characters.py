# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


def lengthOfLongestSubstring(s: str) -> int:
    # Return zero if s is empty
    if not s:
        return 0

    max_length = 0

    for i in range(len(s)):
        next_letter = s[i+1:].find(s[i]) + 1
        
        length = len(s[i:next_letter] if next_letter else s[i:])

        if length > max_length:
            max_length = length

    return max_length



print(lengthOfLongestSubstring(s="abcabcbb"))