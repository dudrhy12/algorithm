def solution(triangle):
    dp = [[-1] * len(row) for row in triangle]

    answer = dfs(triangle, dp, 0, 0)

    return answer


def dfs(tmp, dp, x, y):
    if x == len(tmp) - 1:
        return tmp[x][y]

    if dp[x][y] != -1:
        return dp[x][y]

    left = dfs(tmp, dp, x + 1, y)
    right = dfs(tmp, dp, x + 1, y + 1)

    dp[x][y] = tmp[x][y] + max(left, right)

    return dp[x][y]