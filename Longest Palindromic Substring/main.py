class Solution(object):
    def is_palindrome(self, s):
        return s == s[::-1]
    def longestPalindrome(self, s):
        current_longest_string = ""
        current_longest_length = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.is_palindrome(s[i : j + 1]) and current_longest_length < j - i + 1:
                    current_longest_string = s[i : j + 1]
                    current_longest_length = j - i + 1
        return current_longest_string