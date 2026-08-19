class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row=len(text1)+1
        cols=len(text2)+1
        dp=[[0 for i in range(cols)]for j in range(row)]
        for r in range(1,row):
            for k in range(1,cols):
                if text1[r-1] == text2[k-1]:
                    dp[r][k] = dp[r-1][k-1] +1
                else:
                    dp[r][k]=max(dp[r-1][k],dp[r][k-1])
        return dp[row-1][cols-1]