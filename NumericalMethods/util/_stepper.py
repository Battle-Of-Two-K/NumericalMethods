def get_solution(method, *args, **kwargs):
    solution = None
    decision = method(*args, **kwargs)
    for step in decision:
        solution = step.get('Решение')
    return solution
