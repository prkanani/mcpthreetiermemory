def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    # Create a DP table to store lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp table from bottom up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS from the dp table
    index = dp[m][n]
    lcs = [''] * index

    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcs)


if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(f"Longest Common Subsequence of '{X}' and '{Y}' is '{longest_common_subsequence(X, Y)}'")
