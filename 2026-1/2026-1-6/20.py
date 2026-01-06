class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        closeOpen = {")" : "(", "]" : "[", "}" : "{"}

        for closed in s:
            if closed in closeOpen:
                if stack and stack[-1] == closeOpen[closed]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(closed)
        
        return True if not stack else False