from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        my_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"                      
        }

        if not digits:
            return []

        # Create a list of strings where each string is the letters for one digit
        inpstr = []
        for i in digits:
            inpstr.append(my_dict[i])

        combinations = []

        def backtrack(index, path):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return

            for letter in inpstr[index]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return combinations