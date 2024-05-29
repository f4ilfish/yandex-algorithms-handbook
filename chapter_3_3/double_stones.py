from enum import Enum

n, m = map(int, input().split())


class GameResultType(str, Enum):
    WIN = "Win"
    LOOSE = "Loose"


answer_matrix = [[GameResultType.LOOSE for _ in range(n + 1)] for _ in range(m + 1)]

for i in range(1, n + 1):
    if answer_matrix[0][i - 1] == GameResultType.WIN:
        answer_matrix[0][i] = GameResultType.LOOSE
    else:
        answer_matrix[0][i] = GameResultType.WIN

for j in range(1, m + 1):
    if answer_matrix[j - 1][0] == GameResultType.WIN:
        answer_matrix[j][0] = GameResultType.LOOSE
    else:
        answer_matrix[j][0] = GameResultType.WIN

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (answer_matrix[j - 1][i - 1] == GameResultType.WIN
                and answer_matrix[j - 1][i] == GameResultType.WIN
                and answer_matrix[j][i - 1] == GameResultType.WIN):
            answer_matrix[j][i] = GameResultType.LOOSE
        else:
            answer_matrix[j][i] = GameResultType.WIN

print(answer_matrix[m][n].value)
