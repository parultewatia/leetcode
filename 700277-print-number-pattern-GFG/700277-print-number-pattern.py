class Solution:
    def printPat(self, n):
        ans = []

        for i in range(n, 0, -1):
            for j in range(n, 0, -1):
                ans.extend([j] * i)
            ans.append(-1)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna