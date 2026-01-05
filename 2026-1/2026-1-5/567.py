class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matching = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matching += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if matching == 26:
                return True

            # add right character
            idx = ord(s2[right]) - ord('a')
            s2Count[idx] += 1
            if s1Count[idx] == s2Count[idx]:
                matching += 1
            elif s1Count[idx] + 1 == s2Count[idx]:
                matching -= 1

            # remove left character
            idx = ord(s2[left]) - ord('a')
            s2Count[idx] -= 1
            if s1Count[idx] == s2Count[idx]:
                matching += 1
            elif s1Count[idx] - 1 == s2Count[idx]:
                matching -= 1

            left += 1

        return matching == 26
