from collections import namedtuple
from enum import Enum
from typing import List


class PegType(int, Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4


Move = namedtuple('Move', ['from_peg', 'to_peg'])

