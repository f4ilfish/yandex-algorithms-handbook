from typing import List

_ = input()

numbers: List[int] = list(map(int, input().split()))

less: List[int] = []
more: List[int] = []

pivot_number = numbers[0]

for number in numbers:
    if number <= pivot_number:
        less.append(number)
    else:
        more.append(number)

less[0], less[-1] = less[-1], less[0]

less.extend(more)

print(" ".join(map(str, less)))
