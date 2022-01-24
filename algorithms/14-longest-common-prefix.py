'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

'''
Time O(1)
Space: O(1)
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        key = min(strs, key=len)
        strs.remove(key)
        while len(key) > 0:
            x = 0
            for s in strs:
                if not s.startswith(key):
                    break
                x += 1
            if x == len(strs):
                return key
            key = key[:-1]
        return ""
    
