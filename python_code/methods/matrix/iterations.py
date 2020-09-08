def simple_iterations(matrix, free_column, await_e=(10 ** -8), stop_level=None, print_middle_values=False):
    """Метод простых итераций"""
    matrix = matrix.copy()
    free_column = free_column.copy()
    if not matrix.is_dominant:
        raise ArithmeticError("Метод итераций работаеттолько с матрицами с доминантной диагональю")
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
    # Вычисление нормы (минимальная из двух)
    norma = min(matrix.norma_1, matrix.norma_2)
    # Норма вектора свободных членов
    free_norm = max(map(lambda x: abs(x), free_column))
    # Принимаем за начальный вектор вектор бета с шапкой
    solution_vector = free_column.copy()
    matrix.append_column(free_column.copy())
    solution_vector.append(1)
    # Входим в цикл
    iteration_counter = 1
    delta = 'Неизвестно'
    while True:
        if print_middle_values:
            print(f'''Номер итерации: {iteration_counter}
        X: {round(solution_vector[0], 8)}; Y: {round(solution_vector[1], 8)}; Z: {round(solution_vector[2], 8)}
        E: {round((norma ** (iteration_counter - 2)) / (1 - norma) / 10, 8)}, delta: {delta}\n''')
        if stop_level:
            if iteration_counter == stop_level:
                break
        if await_e > (norma ** (iteration_counter - 2)) / (1 - norma) / 10:
            break
        new_solution = []
        for row_no in range(matrix.rows):
            container = 0
            for col_no in range(matrix.columns):
                container += solution_vector[col_no] * matrix[row_no][col_no]
            new_solution.append(container)
        new_solution.append(1)
        delta = round(max(map(lambda x: abs(x), [_ - __ for _, __ in zip(solution_vector, new_solution)])), 8)
        solution_vector = new_solution
        iteration_counter += 1
    return solution_vector[:-1]


def zeidel_method(matrix, free_column, await_e=(10 ** -8), stop_level=None, print_middle_values=False):
    """Метод Зейделя"""
    # TODO: Исправить
    matrix = matrix.copy()
    free_column = free_column.copy()
    if not matrix.is_dominant:
        raise ArithmeticError("Метод итераций работаеттолько с матрицами с доминантной диагональю")
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
    # Вычисление нормы (минимальная из двух)
    norma = min(matrix.norma_1, matrix.norma_2)
    # Норма вектора свободных членов
    free_norm = max(map(lambda x: abs(x), free_column))
    # Принимаем за начальный вектор вектор бета с шапкой
    solution_vector = free_column.copy()
    matrix.append_column(free_column.copy())
    solution_vector.append(1)
    # Входим в цикл
    iteration_counter = 1
    delta = 'Неизвестно'
    while True:
        old_solution = solution_vector.copy()
        if print_middle_values:
            print(f'''Номер итерации: {iteration_counter}
            X: {round(solution_vector[0], 8)}; Y: {round(solution_vector[1], 8)}; Z: {round(solution_vector[2], 8)}
            E: {round((norma ** (iteration_counter - 2)) / (1 - norma) / 10, 8)}, delta: {delta}\n''')
        if stop_level:
            if iteration_counter == stop_level:
                break
        if await_e > (norma ** (iteration_counter - 2)) / (1 - norma) / 10:
            break
        for row_no in range(matrix.rows):
            container = 0
            for col_no in range(matrix.columns):
                val_add = solution_vector[col_no] * matrix[row_no][col_no]
                container += val_add
            solution_vector[row_no] = container
        delta = round(max(map(lambda x: abs(x), [_ - __ for _, __ in zip(solution_vector, old_solution)])), 8)
        iteration_counter += 1
    return solution_vector[:-1]
