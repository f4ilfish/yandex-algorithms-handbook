n = int(input())

numbers = list(map(int, input().split()))

for i in range(len(numbers) - 1):
    for j in range(i, len(numbers)):
        if numbers[j] < numbers[i]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(" ".join(map(str, numbers)))
