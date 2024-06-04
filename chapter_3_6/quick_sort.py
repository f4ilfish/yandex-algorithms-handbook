import random
from typing import List


def quick_sort(numbers: List[int]) -> List[int]:

    if len(numbers) < 2:
        return numbers
    else:
        random_index = random.randint(a=0, b=(len(numbers) - 1))
        pivot_number = numbers.pop(random_index)

        less: List[int] = []
        more: List[int] = []

        for number in numbers:
            if number <= pivot_number:
                less.append(number)
            else:
                more.append(number)

        return quick_sort(less) + [pivot_number] + quick_sort(more)


_ = input()
impute_numbers = list(map(int, input().split()))
sorted_numbers = quick_sort(impute_numbers)
print(" ".join(map(str, sorted_numbers)))
