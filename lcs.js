/*
 * Longest Common Subsequence (LCS) Dynamic Programming Implementation
 *
 * This script defines a function to compute the length of the LCS between two strings
 * and also reconstructs one LCS sequence.
 *
 * Usage example:
 *   node lcs.js
 */

function longestCommonSubsequence(text1, text2) {
  const m = text1.length;
  const n = text2.length;
  // dp[i][j] will hold the length of LCS of text1[0..i-1] and text2[0..j-1]
  const dp = Array(m + 1)
    .fill(null)
    .map(() => Array(n + 1).fill(0));

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (text1[i - 1] === text2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
      } else {
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }

  // Reconstruct one LCS from the dp table
  let i = m, j = n;
  let lcs = [];
  while (i > 0 && j > 0) {
    if (text1[i - 1] === text2[j - 1]) {
      lcs.push(text1[i - 1]);
      i--;
      j--;
    } else if (dp[i - 1][j] > dp[i][j - 1]) {
      i--;
    } else {
      j--;
    }
  }

  lcs = lcs.reverse().join('');

  return { length: dp[m][n], sequence: lcs };
}

// Example usage
const str1 = 'AGGTAB';
const str2 = 'GXTXAYB';
const result = longestCommonSubsequence(str1, str2);
console.log(`Longest Common Subsequence length: ${result.length}`);
console.log(`Longest Common Subsequence: ${result.sequence}`);

module.exports = { longestCommonSubsequence };