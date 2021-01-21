def power(list_, value):
    summa = 0
    for step in list_:
        summa += step * value
    return summa


def pow_with_vector_v(matrix, norm_vector):
    # TODO: Костыль!!! Переделать!!!
    solution = []
    a = power(matrix[0], norm_vector[0])
    b = power(matrix[1], norm_vector[1])
    c = power(matrix[2], norm_vector[2])

    solution.append(a)
    solution.append(b)
    solution.append(c)

    # gen = 0
    # solution_ = []
    # for step in matrix:
    #     while gen <= len(norm_vector) - 1:
    #         solution_.append(power(step, norm_vector[gen]))
    #         gen += 1

    return solution


def rounded_list(values: list, quantity: int = 9):
    """
    Округление элементов списка.

    Args:
        values (list): список значений
        quantity (int): точность округления
    Returns:
        list: список с округлёнными элементами

    """
    return [round(value, quantity) for value in values]


def ro(list_1, list_2):
    # TODO: Костыль!!! Переделать!!!
    a = list_1[0] * list_2[0]
    b = list_1[1] * list_2[1]
    c = list_1[2] * list_2[2]

    result = a + b + c

    return result


def euclid_norm(list_):
    result = 0
    for step in list_:
        result += step ** 2
    result = result ** .5
    return result


if __name__ == '__main__':
    mat = [[-12, 4, 8],
           [4, 11, -6],
           [8, -6, 2]]

    norm = [1 / (3 ** .5), 1 / (3 ** .5), 1 / (3 ** .5)]

    nu = rounded_list(pow_with_vector_v(mat, norm))
    print(nu)
    ro = ro(nu, norm)
    print(ro)
    nuE = euclid_norm(nu)
    print(nuE)
    solution = [nu[0] / nuE, nu[1] / nuE, nu[2] / nuE]
    print(solution)

    nu1 = rounded_list(pow_with_vector_v(mat, solution))
    print(nu1)
    ro1 = ro(nu1, solution)
    print(ro1)
    nuE1 = euclid_norm(nu1)
    print(nuE1)
    solution1 = [nu1[0] / nuE1, nu1[1] / nuE1, nu1[2] / nuE1]
    print(solution1)





