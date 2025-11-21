# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/description/


def longestPalindrome(s: str) -> str:

    for i in range(len(s)):
        if len(s) % 2 != 0:
            start = len(s) // 2 - 1
            end = len(s) // 2 + 2
        else:
            start = len(s) // 2 - 1
            end = len(s) // 2 + 1



print(longestPalindrome(s="babad")) # "bab" or "aba"
# print(longestPalindrome(s="a")) # "a"
# print(longestPalindrome(s="qqq")) # qqq
# print(longestPalindrome(s="qwerty"))
# print(longestPalindrome(s="wcqdyulxbzrabuvjjouvlmbzsfpcykmmusxdgrrirljrltlnswqqgyukxjfhzhbpipkswzqroarikxtrlzjriyivdjydlfopqnbqlwiperuaeszhthcunyqejayftrlwiucvlghkurgmnlixfoaokgvucdgzscjkwleifdkjycrgwidibldabhsquotljtvjxitfyrvvwlzxavvgjkmtxswxhutxgeaajuycqpxjraxgsixtmncwauubigsxdjzmgpdwvfztuzsxwyiwjeuzapjmbpfhcdzptmcphjtzdwdlpzzqnomamykbxmsbirtxjqfylatgzzelunzgomohgmlirxkgxregmbhwpoovormmvfrhqoovewpwukfdfxlmqdcvkvjueqrkmsgraexfhdstjaxqxwfbhbuvbnyxckefikkyblrfdrsdgyjckhblycffuqfsrlsenyluxepmscukwruipanugiakyrmmvrcjsgyprrke"))
