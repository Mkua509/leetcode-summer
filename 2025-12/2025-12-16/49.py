from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        word_map = defaultdict(list)
        result = []

        # Word being current word in strings list
        for word in strs:
            # Sort them in alphabetical order
                # Mutabble data types cannot be keys s must be a immutable Data type like a tupple
                sorted_string = tuple(sorted(word))
                word_map[sorted_string].append(word)
        for value in word_map.values():
             result.append(value)
        
        return result
        

