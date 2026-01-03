class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Symbol = ["I", "V", "X", "L", "C", "D", "M"]
        Value = [1, 5, 10, 50, 100, 500, 1000]
        Combine = []
        for i in range(len(Symbol)):
            Combine.append((Symbol[i], Value[i]))
        
        roman_map = dict(Combine)

        total = 0
        prev_value = 0

        for char in reversed(s):
            curr_value = roman_map[char]
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value
            prev_value = curr_value
        return total

        