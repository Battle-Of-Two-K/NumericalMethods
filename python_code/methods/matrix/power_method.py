def power_method(matrix, await_d=None, iterations=None, level_of_detail=3):
    """Степенной метод вычисления спектрального радиуса"""
    matrix = matrix.copy()
    answer = {}
    if level_of_detail < 2:
        answer.update({'Этап': 'Получены данные', 'Матрица': matrix})
        yield answer
    # Установка точки остановки цикла
    if await_d is None and iterations is None:
        await_d = 10 ** (-8)
    # Получение нормированного вектора нужного размера и сразу транспонирование
    # (дальнейшие вычисления в "вертикальном режиме")
    omega = matrix.vector_get_norm_3_vector(matrix.columns).T
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
        ro = v.vector_scalar_mul(omega)
        if level_of_detail < 3:
            answer.update({'Номер итерации': iteration_counter})
            answer.update({f'w{iteration_counter}': omega.vector_to_list})
        omega = v / v.vector_norm_3
        delta = abs(old_ro - ro) if old_ro else None
        old_ro = ro
        iteration_counter += 1
        if level_of_detail < 3:
            answer.update({
                f'v{iteration_counter}': v.vector_to_list,
                'p': ro,
                'Дельта': delta
            })
            yield answer
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
