def convert(word1, word2):
    row_size, col_size = len(word1),len(word2)
    dp = [[0]*(col_size+1) for _ in range(row_size+1)]
    for col in range(len(dp[0])):dp[0][col]=col
    for row in range(len(dp)):dp[row][0]=row
    for row in range(1,len(dp)):
        for col in range(1,len(dp[row])):
            if word1[row-1]==word2[col-1]:
                dp[row][col]=dp[row-1][col-1]
            else:
                dp[row][col] = 1 + min(
                    dp[row-1][col],dp[row-1][col-1],dp[row][col-1]
                )
    return dp[row_size][col_size]

# Example usage
word1 = "horse"
word2 = "rose"
print(convert(word1, word2))  # Expected Output: 2