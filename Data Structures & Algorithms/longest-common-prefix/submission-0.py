class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ruler = strs[0]

        for i in range(len(ruler)):
            for word in strs:
                if i == len(word) or word[i] != ruler[i]:
                    return ruler[:i]
        return ruler
            
            
            