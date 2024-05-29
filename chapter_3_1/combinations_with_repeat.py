def get_n_k_combinations_with_repeat(n, k):
    combinations = 1

    for i in range(1, n + k):
        combinations *= i

        if i <= k:
            combinations /= i

        if i <= (n - 1):
            combinations /= i

    return int(combinations)


n, k = map(int, input().split())
print(get_n_k_combinations_with_repeat(n, k))
