class TimeMap(object):

    def __init__(self):
        self.store = {} # key : value=[list of [value, timestamp]]
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        result = ""
        values = self.store.get(key, [])

        # Binary search

        left, right = 0, len(values) - 1
        while left <= right:
            middle = (left + right) // 2
            if values[middle][1] <= timestamp:
                result = values[middle][0]
                left = middle + 1
            else:
                right = middle - 1

        return result
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)