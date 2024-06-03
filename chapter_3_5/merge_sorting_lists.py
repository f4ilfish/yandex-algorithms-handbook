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


n = int(input())

sequences: List[List[int]] = []

for _ in range(n):
    _ = input()
    sequence: List[int] = list(map(int, input().split()))
    sequence.sort()
    sequences.append(sequence)

while len(sequences) != 1:
    merged_sequence: List[int] = merge(sequences.pop(), sequences.pop())
    sequences.append(merged_sequence)

print(" ".join(map(str, sequences[0])))
