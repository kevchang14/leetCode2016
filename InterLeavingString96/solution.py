class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        s1 += " "
        s2 += " "
        s3 += " "
        results = [["" for j in range(0, len(s2) + 1)] for x in range(0, len(s1) + 1)]

        results = self.insertNewLetter(s1, s2, s3, 0, 0, results)

        j = 0
        for i in range(1, len(s1)):
            if results[i - 1][j] is not None and results[i][j] is not None:
                results = self.insertNewLetter(s1, s2, s3, i, j, results)
            else:
                results[i][j] = None

        i=0
        for j in range(1, len(s2)):
            if results[i][j - 1] is not None and results[i][j] is not None:
                results = self.insertNewLetter(s1, s2, s3, i, j, results)
            else:
                results[i][j] = None

        for i in range(1, len(s1)):
            for j in range(1, len(s2)):
                if results[i - 1][j] is not None or results[i][j - 1] is not None:
                    results = self.insertNewLetter(s1, s2, s3, i, j, results)
                else:
                    results[i][j] = None
        return results[len(s1) - 1][len(s2) - 1] is not None


    def insertNewLetter(self, s1, s2, s3, i, j, results):
        if results[i][j] is None:
            return results
        elif s1[i] == s3[i + j] and s2[j] == s3[i + j]:
            results[i][j] = s1[i]
        elif s1[i] == s3[i + j]:
            results[i][j] = s1[i]
            results[i][j + 1] = None
        elif s2[j] == s3[i + j]:
            results[i][j] = s2[j]
            results[i + 1][j] = None
        else:
            results[i][j] = None
        return results