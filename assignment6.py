weights = [3,2,5,1]
values = [62,31,21,71]
capacity = 6

n = len(weights)

#MEMOIZATION

memo = {}

def knapsack_memo(n, capacity):

    # Base condition
    if n == 0 or capacity == 0:
        return 0

    # Check if already calculated
    if (n, capacity) in memo:
        return memo[(n, capacity)]

    # If item cannot fit
    if weights[n - 1] > capacity:
        memo[(n, capacity)] = knapsack_memo(n - 1, capacity)

    else:
        # Include item
        include = values[n - 1] + knapsack_memo(
            n - 1,
            capacity - weights[n - 1]
        )

        # Exclude item
        exclude = knapsack_memo(n - 1, capacity)

        # Store maximum
        memo[(n, capacity)] = max(include, exclude)

    return memo[(n, capacity)]


memo_result = knapsack_memo(n, capacity)

# TABULATION

dp = [[0] * (capacity + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, capacity + 1):

        # If item can fit
        if weights[i - 1] <= w:

            # Take the item
            take = values[i - 1] + dp[i - 1][w - weights[i - 1]]

            # Do not take the item
            not_take = dp[i - 1][w]

            dp[i][w] = max(take, not_take)

        else:
            dp[i][w] = dp[i - 1][w]


tabulation_result = dp[n][capacity]

print("Memoization:", memo_result)
print("Tabulation:", tabulation_result)