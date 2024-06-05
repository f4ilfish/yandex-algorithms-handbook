from typing import List

n, m = map(int, input().split())

matrix_a: List[List[int]] = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix_a.append(row)

matrix_b: List[List[int]] = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix_b.append(row)

matrix_c: List[List[int]] = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        matrix_c[i][j] = matrix_a[i][j] + matrix_b[i][j]

for row in matrix_c:
    print(" ".join(map(str, row)))
