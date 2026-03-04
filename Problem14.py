#from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Initialize the common prefix as an empty string
        common_prefix = ""
        
        # Find the length of the shortest string
        min_length = min(len(s) for s in strs)
        
        # Iterate over each character position (up to the shortest string's length)
        for c in range(min_length):
            # Check if all strings have the same character at position `c`
            current_char = strs[0][c]  # Take the character from the first string
            if all(s[c] == current_char for s in strs):
                common_prefix += current_char  # Append the character to the prefix
            else:
                break  # Stop if a mismatch is found

        return common_prefix