class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0
        seen = set()
        i = 0
        j = 0

        while  j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1

            seen.add(s[j])
            longest = max(j-i+1, longest)
            j += 1
        return longest
        