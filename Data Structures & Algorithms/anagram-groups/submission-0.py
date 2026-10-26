class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            label = "".join(sorted(word))
            if label in groups:
                groups[label].append(word)
            else:
                groups[label] = [word]

        return list(groups.values())
        