try:
    from sympy import lambdify, diff, simplify, pretty, solve, symbols, evalf
    from sympy import Symbol, Pow, Add, Mul
    from sympy.parsing.sympy_parser import parse_expr
    from sympy.plotting import plot, plot_parametric
    x, y = symbols('x y')
except ModuleNotFoundError:
    try:
        print(f'\n{" Фрагмент программы не найден, устанавливается, это займет поределенное время ".center(100, "!")}',
              end='\n\n')
        import os
        os.system('pip install sympy')
        os.system('pip3 install sympy')
        from sympy import lambdify, diff, simplify, pretty, solve, symbols, evalf
        from sympy import Symbol, Pow, Add, Mul
        from sympy.parsing.sympy_parser import parse_expr
        from sympy.plotting import plot, plot_parametric
        x, y = symbols('x y')
        print(f'\n\n{" Все готово, решаю задание... ".center(100, "=")}\n\n')
    except Exception as error:
        input(str(error))


def find_symbols(expr):
    action_list = [Pow, Add, Mul]
    symbols_list = set()
    for arg in expr.args:
        if isinstance(arg, Symbol):
            symbols_list.update({arg})
        else:
            for action in action_list:
                if isinstance(arg, action):
                    symbols_list.update(find_symbols(arg))
    return symbols_list


def parse_list(target_list):
    return [simplify(parse_expr(target)) for target in target_list]
