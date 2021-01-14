def get_solution(decision):
    solution = None
    for step in decision:
        solution = step.get('Решение')
    return solution
