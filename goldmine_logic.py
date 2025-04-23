def max_gold_with_path(gold):
    n = len(gold)
    m = len(gold[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    path = [[[] for _ in range(m)] for _ in range(n)]

    for col in range(m - 1, -1, -1):
        for row in range(n):
            right = dp[row][col + 1] if col != m - 1 else 0
            right_up = dp[row - 1][col + 1] if row > 0 and col != m - 1 else 0
            right_down = dp[row + 1][col + 1] if row < n - 1 and col != m - 1 else 0

            max_val = max(right, right_up, right_down)

            dp[row][col] = gold[row][col] + max_val

            if col == m - 1:
                path[row][col] = [(row, col)]
            else:
                if max_val == right:
                    path[row][col] = [(row, col)] + path[row][col + 1]
                elif max_val == right_up:
                    path[row][col] = [(row, col)] + path[row - 1][col + 1]
                else:
                    path[row][col] = [(row, col)] + path[row + 1][col + 1]

    max_val = 0
    final_path = []
    for row in range(n):
        if dp[row][0] > max_val:
            max_val = dp[row][0]
            final_path = path[row][0]

    return max_val, dp, final_path
