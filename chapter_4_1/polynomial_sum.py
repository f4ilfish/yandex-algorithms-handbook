n = int(input())
a_ratio = list(map(int, input().split()))
a_ratio.reverse()

m = int(input())
b_ratio = list(map(int, input().split()))
b_ratio.reverse()


result_ratio = [0 for _ in range(max(len(a_ratio), len(b_ratio)))]

for i in range(max(len(a_ratio), len(b_ratio))):
    if i < len(a_ratio):
        result_ratio[i] += a_ratio[i]
    if i < len(b_ratio):
        result_ratio[i] += b_ratio[i]

result_ratio.reverse()

print(max(n, m))

print(" ".join(map(str, result_ratio)))
