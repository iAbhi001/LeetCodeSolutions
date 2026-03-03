class Solution:
    def intToRoman(self, num: int) -> str:
        inverse_hash_map = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
            10: "X",
            20: "XX",
            30: "XXX",
            40: "XL",
            50: "L",
            60: "LX",
            70: "LXX",
            80: "LXXX",
            90: "XC",
            100: "C",
            200: "CC",
            300: "CCC",
            400: "CD",
            500: "D",
            600: "DC",
            700: "DCC",
            800: "DCCC",
            900: "CM",
            1000: "M",
            2000: "MM",
            3000: "MMM"
        }

        res = []
        i = 0
        while num > 0:
            digit = num % 10
            if digit != 0:
                res.append(digit * (10 ** i))
            num //= 10
            i += 1

        res.reverse()  # Now digits are in left-to-right order

        roman_str = ""
        for val in res:
            roman_str += inverse_hash_map[val]
        return roman_str
