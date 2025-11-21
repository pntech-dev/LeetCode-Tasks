# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0

    substrings = []

    for i in range(len(s)):
        substring = s[i]

        for j in range(len(s)):
            if j == i or j < i:
                continue

            if s[j] not in substring:
                substring += s[j]
            else:
                substrings.append(substring)
                break

        substrings.append(substring)

    return max([len(sub) for sub in substrings])



print(lengthOfLongestSubstring(s="abcabcbb")) # "abc" or "bca" or "cab" - 3
print(lengthOfLongestSubstring(s="bbbbb")) # "b" - 1
print(lengthOfLongestSubstring(s="pwwkew")) # "wke"
print(lengthOfLongestSubstring(s=" ")) # [] - 1
print(lengthOfLongestSubstring(s="au")) # "au" - 2
print(lengthOfLongestSubstring(s="dvdf")) # "vdf" - 3 