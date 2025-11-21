# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/


def longestCommonPrefix(strs: list[str]) -> str:
    # Return an empty string if the strs list is empty, or if all items in the list are empty
    if not strs or not all(s.strip() for s in strs) or not all(s[0] == strs[0][0] for s in strs):
        return ""

    # We define a prefix from the first word with the length of the smallest word
    prefix = strs[0][0:min([len(word) for word in strs])]

    # While not all strings in the list start with a prefix
    while not all(s.startswith(prefix) for s in strs):
        prefix = prefix[0:len(prefix)-1] # Remove the last letter from the prefix
    
    return prefix


print(longestCommonPrefix(strs=["a"]))
print(longestCommonPrefix(strs=["flower","flow","flight"]))
print(longestCommonPrefix(strs=["dog","racecar","car"]))
print(longestCommonPrefix(strs=["cir","car"]))
print(longestCommonPrefix(strs=["flower","fkow"]))