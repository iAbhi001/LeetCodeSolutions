class Solution:
    def romanToInt(self, s: str) -> int:
        di = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        integer = 0
        i = 0
        while i < len(s):
            # Check if the next character exists and the current value is less than the next value
            if i + 1 < len(s) and di[s[i]] < di[s[i + 1]]:
                # Subtract the current value from the next value and add the result
                integer += di[s[i + 1]] - di[s[i]]
                i += 2  # Skip the next character since it's already processed
            else:
                # Add the value of the current numeral
                integer += di[s[i]]
                i += 1

        return integer