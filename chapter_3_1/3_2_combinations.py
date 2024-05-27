# https://youtu.be/yTIRwioT8W4

def get_n_k_combinations(n, k):
    if n < k:
        return 0

    combinations = 1

    for i in range(1, n + 1):
        combinations *= i

        if i <= k:
            combinations /= i

        if i <= (n - k):
            combinations /= i

    return int(combinations)


n, k = map(int, input().split())
print(get_n_k_combinations(n, k))
