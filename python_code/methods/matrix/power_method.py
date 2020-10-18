

def power_method(matrix,
                 await_d: (int, float) = None,
                 iterations: int = None,
                 level_of_detail: int = 3):
    """
    Степенной метод вычисления спектрального радиуса

    Args:
        matrix (Matrix): матрица, радиус которой необходимо найти
        await_d (int, float): ожидаемая дельта
        iterations (int): необходимое количество итераций
        level_of_detail (int): уровень детализации (меньше число - больше деталей)

    Yields:
        dict: данные о текущем шаге решения

    """
    matrix = matrix.копия()
    answer = {}
    if level_of_detail < 2:
        answer.update({'Этап': 'Получены данные', 'Матрица': matrix})
        yield answer
    # Установка точки остановки цикла
    if await_d is None and iterations is None:
        await_d = 10 ** (-8)
    # Получение нормированного вектора нужного размера и сразу транспонирование
    # (дальнейшие вычисления в "вертикальном режиме")
    omega = matrix.получить_нормированный_по_3_норме_вектор(matrix.количество_столбцов).транспонированная
    if level_of_detail < 2:
        answer.update({'Этап': 'Создан нормированный вектор', 'Нормированный вектор (омега)': omega})
        yield answer
    old_ro = None
    iteration_counter = 0
    answer.pop('Этап', None)
    answer.pop('Матрица', None)
    answer.pop('Нормированный вектор (омега)', None)
    while True:
        # Далее согласно методичке
        v = matrix * omega
        # Скалярное произведение (ro = (v, omega))
        ro = v.скалярное_произведение_векторов(omega)
        if level_of_detail < 3:
            answer.update({'Номер итерации': iteration_counter})
            answer.update({f'w{iteration_counter}': omega.вектор_в_список})
        omega = v / v.векторная_норма_3
        delta = abs(old_ro - ro) if old_ro else None
        old_ro = ro
        iteration_counter += 1
        if level_of_detail < 3:
            answer.update({
                f'v{iteration_counter}': v.вектор_в_список,
                'Дельта': delta
            })
            yield answer
            answer.update({'p': ro})
            answer.pop(f'w{iteration_counter - 1}', None)
            answer.pop(f'v{iteration_counter}', None)
        if await_d:
            if delta:
                if delta < await_d:
                    break
        elif iterations:
            if iteration_counter == iterations:
                break
    answer.pop('Номер итерации', None)
    answer.pop('p', None)
    answer.pop('Дельта', None)
    if level_of_detail < 4:
        answer.update({'Решение': ro})
    yield answer
