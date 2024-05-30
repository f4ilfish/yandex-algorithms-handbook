from enum import Enum

n, m = map(int, input().split())


class GameResultType(str, Enum):
    WIN = "Win"
    LOOSE = "Loose"


answer_matrix = [[GameResultType.LOOSE for _ in range(n + 1)] for _ in range(m + 1)]

# Находим и меняем предзаполненные LOOSE случаи ни WIN
for i in range(1, n + 1):
    if i % 3 != 0:
        answer_matrix[0][i] = GameResultType.WIN

# Находим и меняем предзаполненные LOOSE случаи ни WIN
for j in range(1, m + 1):
    if j % 3 != 0:
        answer_matrix[j][0] = GameResultType.WIN

for i in range(1, n + 1):
    for j in range(1, m + 1):

        # По условию задачи можем взять:
        #   1 камень либо с одной, либо с другой кучи
        #   2 камня из одной из куч
        #   2 камня из одной и 1 камень из другой куич
        # Анализируем ячейки в радиусе 1 шага (сверху, слева)
        # Шаги в радиусе 2+ шага для других ходов анализировать не имеет смысла
        # Пользуемся мемоизацией результата (если в радиусе 1 шага все устраивает - ок)

        if (answer_matrix[j - 1][i] == GameResultType.LOOSE
                or answer_matrix[j][i - 1] == GameResultType.LOOSE):
            answer_matrix[j][i] = GameResultType.WIN

print(answer_matrix[m][n].value)
