from collections import namedtuple
from enum import Enum
from typing import List


class PegType(int, Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3


Move = namedtuple('Move', ['from_peg', 'to_peg'])


def get_unused_peg(from_peg: PegType, to_peg: PegType):
    return PegType(6 - from_peg.value - to_peg.value)


def move_disks(
    disks_number: int,
    from_peg: PegType,
    to_peg: PegType,
    iterations: List[Move]
):
    if disks_number == 1:
        iterations.append(Move(from_peg, to_peg))
        return

    unused_peg = get_unused_peg(from_peg, to_peg)
    move_disks(disks_number - 1, from_peg, unused_peg, iterations)
    iterations.append(Move(from_peg, to_peg))
    move_disks(disks_number - 1, unused_peg, to_peg, iterations)


n = int(input())

result_iterations: List[Move] = []
move_disks(n, PegType.FIRST, PegType.THIRD, result_iterations)

print(len(result_iterations))
for iteration in result_iterations:
    print(f"{iteration.from_peg.value} {iteration.to_peg.value}")
