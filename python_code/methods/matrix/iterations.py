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
    if matrix.norma_1 <= matrix.norma_2:
        norma_beta = max(map(lambda x: abs(x), free_column))
    else:
        norma_beta = sum(map(lambda x: abs(x), free_column))
    if print_middle_values:
        print("\nНорма бета: ", norma_beta)
    if print_middle_values:
        print(f"""\nПервая норма матрицы = {round(matrix.norma_1, 8)}; Вторая норма матрицы = {round(matrix.norma_2, 8)}
Минимальная норма = {round(norma, 8)}\n""")
    # Норма вектора свободных членов
    free_norm = max(map(lambda x: abs(x), free_column))
    # Принимаем за начальный вектор вектор бета с шапкой
    solution_vector = free_column.copy()
    # Добавление столбца свободных членов
    matrix.append_column(free_column.copy())
    # Добавление единицы нужно для нормальной работы цикла с матрицей с добавленным столбцом свободных членов
    solution_vector.append(1)
    # Входим в цикл
    iteration_counter = 0
    delta = 'Неизвестно'
    while True:
        if print_middle_values:
            print(f'''Номер итерации: {iteration_counter}
        X: {round(solution_vector[0], 8)}; Y: {round(solution_vector[1], 8)}; Z: {round(solution_vector[2], 8)}
        E: {round(((norma ** iteration_counter) / (1 - norma)) * norma_beta, 8)}, delta: {delta}\n''')
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
            # Только после заполнения нового вектора (обработана вся матрица), замняем вектор решений на новый на новый
            new_solution.append(container)
        new_solution.append(1)
        delta = round(max(map(lambda x: abs(x), [_ - __ for _, __ in zip(solution_vector, new_solution)])), 8)
        # Вот и замена
        solution_vector = new_solution
        iteration_counter += 1
    return solution_vector[:-1]


def zeidel_method(matrix, free_column, await_e=(10 ** -8), stop_level=None, print_middle_values=False):
    """Метод Зейделя"""
    # TODO: Исправить
    matrix = matrix.copy()
    free_column = free_column.copy()
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
    # Вычисление нормы (минимальная из двух)
    norma = min(matrix.norma_1, matrix.norma_2)
    if matrix.norma_1 <= matrix.norma_2:
        norma_beta = max(map(lambda x: abs(x), free_column))
    else:
        norma_beta = sum(map(lambda x: abs(x), free_column))
    if print_middle_values:
        print("\nНорма бета: ", norma_beta)
    if print_middle_values:
        print(f"""\nПервая норма матрицы = {round(matrix.norma_1, 8)}; Вторая норма матрицы = {round(matrix.norma_2, 8)} 
Минимальная норма = {round(norma, 8)}\n""")
    # Норма вектора свободных членов
    free_norm = max(map(lambda x: abs(x), free_column))
    # Принимаем за начальный вектор вектор бета с шапкой
    solution_vector = free_column.copy()
    # Добавление столбца свободных членов
    matrix.append_column(free_column.copy())
    # Добавление единицы нужно для нормальной работы цикла с матрицей с добавленным столбцом свободных членов
    solution_vector.append(1)
    # Входим в цикл
    iteration_counter = 0
    delta = 'Неизвестно'
    while True:
        old_solution = solution_vector.copy()
        if print_middle_values:
            print(f'''Номер итерации: {iteration_counter}
            X: {round(solution_vector[0], 8)}; Y: {round(solution_vector[1], 8)}; Z: {round(solution_vector[2], 8)}
            E: {round((norma ** iteration_counter) / (1 - norma) * norma_beta, 8)}, delta: {delta}\n''')
        if stop_level:
            if iteration_counter == stop_level:
                break
        if await_e > (norma ** (iteration_counter - 2)) / (1 - norma) / 10:
            break
        for row_no in range(matrix.rows):
            container = 0
            for col_no in range(matrix.columns):
                container += solution_vector[col_no] * matrix[row_no][col_no]
            # В строке ниже и кроется отличие: для дальнейших вычислений сразу используется полученный результат
            solution_vector[row_no] = container
        delta = round(max(map(lambda x: abs(x), [_ - __ for _, __ in zip(solution_vector, old_solution)])), 8)
        iteration_counter += 1
    return solution_vector[:-1]


def triple_diagonal(matrix, free_column, print_middle_values=False):
    """Метод прогонки. Метод Томаса"""

    def get_element(row, col):
        if 0 < row <= matrix.rows and 0 < col <= matrix.columns - 1:
            return matrix[row - 1][col - 1]
        else:
            return 0

    if not matrix.is_triple_diagonal:
        raise ArithmeticError("Метод прогонки работает только с трехдиагональной марицей")
    matrix = matrix.copy()
    matrix.append_column(free_column)
    if print_middle_values:
        print("Расширенная матрица:")
        matrix.console_display()
    p = [0]
    q = [0]
    # Прямой ход прогонки
    for row_no in range(1, matrix.rows + 1):
        a = get_element(row_no, row_no - 1)
        b = get_element(row_no, row_no)
        c = get_element(row_no, row_no + 1)
        d = matrix[row_no - 1][matrix.columns - 1]
        new_p = -c / (b + a * p[row_no - 1])
        p.append(new_p)
        new_q = (d - a * q[row_no - 1]) / (b + a * p[row_no if row_no < 2 else row_no - 1])
        q.append(new_q)
    if print_middle_values:
        print("Результат прямой прогонки:")
        print('P: ', end='')
        for val in p:
            print(round(val, 8), end=', ')
        print('\nQ: ', end='')
        for val in q:
            print(round(val, 8), end=', ')
        print()
    # Обратный ход прогонки
    x = [0 for row_no in range(matrix.rows + 1)]
    for row_no in range(matrix.rows, 0, -1):
        if row_no == matrix.rows:
            x[row_no] = q[row_no]
        else:
            # Этот if необходим из-за "кривых" индексов
            x[row_no] = q[row_no] + p[row_no] * x[row_no + 1]
    return x[1:]


def auto_iterate(matrix, free_column, await_e=(10 ** -8), stop_level=None, print_middle_values=False):
    """Автоматический выбор лучшего алгоритма"""
    if matrix.is_triple_diagonal:
        return triple_diagonal(matrix, free_column, print_middle_values)
    else:
        return zeidel_method(matrix, free_column, await_e=await_e,
                             stop_level=stop_level, print_middle_values=print_middle_values)
