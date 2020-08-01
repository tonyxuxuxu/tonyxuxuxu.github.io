class Solution:
    def longestPalindrome(self, s):
        start = end = 0
        for i in range(len(s)):
            maxlensodd = self.longestpalindromefrommiddle(i, i, s)
            maxlenseven = self.longestpalindromefrommiddle(i, i+1, s)
            max_len = max(maxlensodd, maxlenseven)
            if max_len > end - start:
                start = int(i - (maxlen)/2 + 1)
                end = int(i + maxlen/2 + 1)
        return s[start: end]

    def longestpalindromefrommiddle(self, left, right, string):
        str_len = len(string)
        while left >=0 and right < str_len and string[left] == string[right]:
            left -= 1
            right += 1
        return right - left - 1

