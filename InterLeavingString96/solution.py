class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        s1Index = 0
        s2Index = 0
        for i, l in enumerate(s3):
            if s1Index < len(s1) and s2Index < len(s2) and s1[s1Index] == l and s2[s2Index] == l:
                return self.isInterleave(s1[s1Index+1:], s2[s2Index:], s3[i+1:]) or \
                        self.isInterleave(s1[s1Index:], s2[s2Index+1:], s3[i+1:])
            elif s1Index < len(s1) and s1[s1Index] == l:
                s1Index += 1
            elif s2Index < len(s2) and s2[s2Index] == l:
                s2Index += 1
            else:
                return False
        return True