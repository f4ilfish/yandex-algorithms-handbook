from typing import List


def merge(first_sequence: List[int], second_sequence: List[int]) -> List[int]:

    sorted_sequence: List[int] = []

    i, j = 0, 0

    while i < len(first_sequence) and j < len(second_sequence):
        if first_sequence[i] < second_sequence[j]:
            sorted_sequence.append(first_sequence[i])
            if i != len(first_sequence):
                i += 1
        else:
            sorted_sequence.append(second_sequence[j])
            if j != len(second_sequence):
                j += 1

    if i == len(first_sequence):
        sorted_sequence.extend(second_sequence[j:])
    else:
        sorted_sequence.extend(first_sequence[i:])

    return sorted_sequence


def merge_sort(sequence: List[int]) -> List[int]:

    if len(sequence) == 1:
        return sequence

    half_index = len(sequence) // 2

    first_half_sequence = sequence[:half_index]
    second_half_sequence = sequence[half_index:]

    sorted_first_half = merge_sort(first_half_sequence)
    sorted_second_half = merge_sort(second_half_sequence)

    return merge(sorted_first_half, sorted_second_half)


n = str(input())

input_sequence = list(map(int, input().split()))
sorted_input_sequence = merge_sort(input_sequence)
print(" ".join(map(str, sorted_input_sequence)))
