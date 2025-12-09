import sys

if __name__ == '__main__':
    input_data = sys.stdin.read().split()

    iterator = iter(input_data)
    try:
        N = int(next(iterator))
    except StopIteration:
        exit(0)

    treats = [int(next(iterator)) for _ in range(N)]

    # dp[left][right] -> max profit for treats[left...right]
    dp = [[0] * N for _ in range(N)]

    # left = right -> last
    for i in range(N):
        dp[i][i] = treats[i] * N

    for length in range(2, N + 1):
        age = N - length + 1  # The current age for a segment of this size

        # Iterate through all valid start positions (left)
        for left in range(N - length + 1):
            right = left + length - 1

            pick_left = (treats[left] * age) + dp[left + 1][right]
            pick_right = (treats[right] * age) + dp[left][right - 1]

            # Store the better choice
            dp[left][right] = max(pick_left, pick_right)

    # max profit for the full range
    print(dp[0][N - 1])