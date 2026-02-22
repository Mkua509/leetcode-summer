class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # sorting where the sorted anagram is the key and hte value is a list filled with the normal word

        from collections import defaultdict

        word_dict = defaultdict(list)

        for word in strs:
            word_sorted = ''.join(sorted(word))
            word_dict[word_sorted].append(word)

        return list(word_dict.values())