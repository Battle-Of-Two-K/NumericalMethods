def simple_iterations(matrix, free_column, await_e=None, iterations=None, level_of_detail=3):
    """Метод простых итераций
    0 - администраторский уровень
    1 - максималььная сводка
    2 - обзор некоторых промежуточных значений
    3 - только ответ"""
    if iterations is None:
        if await_e is None:
            await_e = (10 ** -8)
    matrix = matrix.copy()
    free_column = free_column.copy()
    answer = {}
    if level_of_detail < 2:
        answer.update({'Этап': 'Получены значения'})
        answer.update({'Матрица': matrix})
        answer.update({'Столбец свободных членов': free_column})
        yield answer
    if not matrix.is_dominant:
        raise ArithmeticError("Метод итераций работает только с матрицами с доминантной диагональю")
    # Извлечение главной диагонали, замещая значения нулями
    new_column = []
    for _ in range(matrix.rows):
        for __ in range(matrix.rows):
            if _ == __:
                new_column.append(matrix[_][__])
                matrix.matrix[_][__] = 0
    matrix = -matrix
    # Деление соответствующих строк на значения из диагонали
    for _ in range(matrix.rows):
        for __ in range(matrix.rows):
            matrix.matrix[_][__] /= new_column[_]
    # Деление сободных членов на значения из диагонали
    free_column = [_ / __ for _, __ in zip(free_column, new_column)]
    if level_of_detail < 2:
        answer.update({'Этап': 'Из матрицы извлечена главная диагональ'})
        answer.update({'Матрица': matrix})
        answer.update({'Столбец свободных членов': free_column})
        yield answer
    # Вычисление нормы (минимальная из двух)
    matrix_norms = (matrix.norma_1, matrix.norma_2)
    vector_norms = (max(map(lambda x: abs(x), free_column)), sum(map(lambda x: abs(x), free_column)))
    norm_number = 1 if matrix.norma_1 <= matrix.norma_2 else 2
    if level_of_detail < 3:
        answer.update({'Этап': 'Вычислены необходимые нормы'})
        answer.update({'Нормы матрицы': matrix_norms})
        answer.update({'Нормы вектора': vector_norms})
        answer.update({'Номер выбранной нормы': norm_number})
        yield answer
    norma_beta = vector_norms[norm_number - 1]
    norma = matrix_norms[norm_number - 1]
    # Принимаем за начальный вектор вектор бета с шапкой
    solution_vector = free_column.copy()
    # Добавление столбца свободных членов
    matrix.append_column(free_column.copy())
    # Добавление единицы нужно для нормальной работы цикла с матрицей с добавленным столбцом свободных членов
    solution_vector.append(1)
    # Входим в цикл
    delta = None
    epsilon = None
    iteration_counter = 0
    answer.pop('Этап', None)
    answer.pop('Нормы матрицы', None)
    answer.pop('Нормы вектора', None)
    answer.pop('Номер выбранной нормы', None)
    answer.pop('Матрица', None)
    answer.pop('Столбец свободных членов', None)
    while True:
        if level_of_detail < 3:
            answer.update({'Номер итерации': iteration_counter})
            answer.update({'Решение': solution_vector[:-1]})
            answer.update({'Дельта': delta})
            answer.update({'Эпсилон': epsilon})
            yield answer
        if iterations:
            if iteration_counter == iterations:
                break
        elif await_e > (norma ** (iteration_counter - 2)) / (1 - norma) / 10:
            break
        new_solution = []
        for row_no in range(matrix.rows):
            container = 0
            for col_no in range(matrix.columns):
                container += solution_vector[col_no] * matrix[row_no][col_no]
            # Только после заполнения нового вектора (обработана вся матрица), замняем вектор решений на новый на новый
            new_solution.append(container)
        new_solution.append(1)
        iteration_counter += 1
        epsilon = ((norma ** iteration_counter) / (1 - norma)) * norma_beta
        delta = max(map(lambda x: abs(x), [_ - __ for _, __ in zip(solution_vector, new_solution)]))
        # Вот и замена
        solution_vector = new_solution
    answer.pop('Дельта', None)
    answer.pop('Эпсилон', None)
    answer.pop('Номер итерации', None)
    if level_of_detail < 4:
        answer.update({'Решение': solution_vector[:-1]})
        yield answer


def zeidel_method(matrix, free_column, await_e=None, iterations=None, level_of_detail=3):
    """Метод простых итераций
    0 - администраторский уровень
    1 - максималььная сводка
    2 - обзор некоторых промежуточных значений
    3 - только ответ"""
    if iterations is None:
        if await_e is None:
            await_e = (10 ** -8)
    matrix = matrix.copy()
    free_column = free_column.copy()
    answer = {}
    if level_of_detail < 2:
        answer.update({'Этап': 'Получены значения'})
        answer.update({'Матрица': matrix})
        answer.update({'Столбец свободных членов': free_column})
        yield answer
    if not matrix.is_dominant:
        raise ArithmeticError("Метод итераций работает только с матрицами с доминантной диагональю")
    # Извлечение главной диагонали, замещая значения нулями
    new_column = []
    for _ in range(matrix.rows):
        for __ in range(matrix.rows):
            if _ == __:
                new_column.append(matrix[_][__])
                matrix.matrix[_][__] = 0
    matrix = -matrix
    # Деление соответствующих строк на значения из диагонали
    for _ in range(matrix.rows):
        for __ in range(matrix.rows):
            matrix.matrix[_][__] /= new_column[_]
    # Деление сободных членов на значения из диагонали
    free_column = [_ / __ for _, __ in zip(free_column, new_column)]
    if level_of_detail < 2:
        answer.update({'Этап': 'Из матрицы извлечена главная диагональ'})
        answer.update({'Матрица': matrix})
        answer.update({'Столбец свободных членов': free_column})
        yield answer
    # Вычисление нормы (минимальная из двух)
    matrix_norms = (matrix.norma_1, matrix.norma_2)
    vector_norms = (max(map(lambda x: abs(x), free_column)), sum(map(lambda x: abs(x), free_column)))
    norm_number = 1 if matrix.norma_1 <= matrix.norma_2 else 2
    if level_of_detail < 3:
        answer.update({'Этап': 'Вычислены необходимые нормы'})
        answer.update({'Нормы матрицы': matrix_norms})
        answer.update({'Нормы вектора': vector_norms})
        answer.update({'Номер выбранной нормы': norm_number})
        yield answer
    norma_beta = vector_norms[norm_number - 1]
    norma = matrix_norms[norm_number - 1]
    # Принимаем за начальный вектор вектор бета с шапкой
    solution_vector = free_column.copy()
    # Добавление столбца свободных членов
    matrix.append_column(free_column.copy())
    # Добавление единицы нужно для нормальной работы цикла с матрицей с добавленным столбцом свободных членов
    solution_vector.append(1)
    # Входим в цикл
    delta = None
    epsilon = None
    iteration_counter = 0
    answer.pop('Этап', None)
    answer.pop('Нормы матрицы', None)
    answer.pop('Нормы вектора', None)
    answer.pop('Номер выбранной нормы', None)
    answer.pop('Матрица', None)
    answer.pop('Столбец свободных членов', None)
    while True:
        old_solution = solution_vector.copy()
        if level_of_detail < 3:
            answer.update({'Номер итерации': iteration_counter})
            answer.update({'Решение': solution_vector[:-1]})
            answer.update({'Дельта': delta})
            answer.update({'Эпсилон': epsilon})
            yield answer
        if iterations:
            if iteration_counter == iterations:
                break
        elif await_e > (norma ** (iteration_counter - 2)) / (1 - norma) / 10:
            break
        for row_no in range(matrix.rows):
            container = 0
            for col_no in range(matrix.columns):
                container += solution_vector[col_no] * matrix[row_no][col_no]
            # В строке ниже и кроется отличие: для дальнейших вычислений сразу используется полученный результат
            solution_vector[row_no] = container
        iteration_counter += 1
        epsilon = ((norma ** iteration_counter) / (1 - norma)) * norma_beta
        delta = max(map(lambda x: abs(x), [_ - __ for _, __ in zip(solution_vector, old_solution)]))
    answer.pop('Дельта', None)
    answer.pop('Эпсилон', None)
    answer.pop('Номер итерации', None)
    if level_of_detail < 4:
        answer.update({'Решение': solution_vector[:-1]})
        yield answer


def triple_diagonal(matrix, free_column, level_of_detail=3):
    """Метод прогонки. Метод Томаса"""

    def get_element(row, col):
        if 0 < row <= matrix.rows and 0 < col <= matrix.columns - 1:
            return matrix[row - 1][col - 1]
        else:
            return 0

    answer = {}
    matrix = matrix.copy()

    if level_of_detail < 2:
        answer.update({'Этап': 'Получены значения'})
        answer.update({'Матрица': matrix})
        answer.update({'Столбец свободных членов': free_column})
        yield answer
    if not matrix.is_triple_diagonal:
        raise ArithmeticError("Метод прогонки работает только с трехдиагональной марицей")
    matrix.append_column(free_column)
    if level_of_detail < 2:
        answer.update({'Этап': 'Расширена матрица'})
        answer.update({'Матрица': matrix})
        answer.update({'Столбец свободных членов': free_column})
        yield answer
    p = [0]
    q = [0]
    # Прямой ход прогонки
    for row_no in range(1, matrix.rows + 1):
        if level_of_detail < 3:
            answer.update({'Этап': f'Прямая прогонка {row_no} строка'})
        a = get_element(row_no, row_no - 1)
        b = get_element(row_no, row_no)
        c = get_element(row_no, row_no + 1)
        d = matrix[row_no - 1][matrix.columns - 1]
        new_p = -c / (b + a * p[row_no - 1])
        if level_of_detail < 2:
            answer.update({'a': a})
            answer.update({'b': b})
            answer.update({'c': c})
            answer.update({'d': d})
            answer.update({"Этап решения": f'P{row_no} = -c / (b + a * P{row_no - 1}) = '
                                           f'P{row_no} = {-c} / ({b} + {a} * {p[row_no - 1]}) = '
                                           f'{new_p}'})
        if level_of_detail < 3:
            answer.update({f'P{row_no}': new_p})
        p.append(new_p)
        new_q = (d - a * q[row_no - 1]) / (b + a * p[row_no if row_no < 2 else row_no - 1])
        if level_of_detail < 2:
            answer.update({"Этап решения": f'Q{row_no} = (d - a * Q{row_no - 1}) / '
                                           f'(b + a * P{row_no if row_no < 2 else row_no - 1}) = '
                                           f'({d} - {a} * {q[row_no - 1]}) / '
                                           f'({b} + {a} * {p[row_no if row_no < 2 else row_no - 1]}) = '
                                           f'{new_q}'})
        if level_of_detail < 3:
            answer.update({f'Q{row_no}': new_q})
        q.append(new_q)
        if level_of_detail < 3:
            yield answer
    # Обратный ход прогонки
    answer.pop('a', None)
    answer.pop('b', None)
    answer.pop('c', None)
    answer.pop('d', None)
    answer.pop('Этап решения', None)
    x = [0 for row_no in range(matrix.rows + 1)]
    for row_no in range(matrix.rows, 0, -1):
        if level_of_detail < 3:
            answer.update({'Этап': f'Обратная прогонка {row_no} строка'})
        if row_no == matrix.rows:
            if level_of_detail < 2:
                answer.update({f'Этап решения': f"X{row_no} = Q{row_no} = {q[row_no]}"})
            x[row_no] = q[row_no]
        else:
            # Этот if необходим из-за "кривых" индексов
            x[row_no] = q[row_no] + p[row_no] * x[row_no + 1]
            if level_of_detail < 2:
                answer.update({f'Этап решения': f"X{row_no} = Q{row_no} + P{row_no} * X{row_no + 1} = "
                                                f"{q[row_no]} + {p[row_no]} * {x[row_no + 1]} = {x[row_no]}"})
        if level_of_detail < 3:
            answer.update({f"X{row_no}": x[row_no]})
            yield answer
    answer.pop('Этап решения', None)
    if level_of_detail < 4:
        answer.update({'Этап': 'Решение получено'})
        answer.update({'Решение': x[1:]})
        yield answer


def auto_iterate(matrix, free_column, await_e=None, iterations=None, level_of_details=3):
    """Автоматический выбор лучшего алгоритма"""
    if matrix.is_triple_diagonal:
        return triple_diagonal(matrix, free_column, level_of_details)
    else:
        return zeidel_method(matrix, free_column, await_e=await_e, iterations=iterations)
