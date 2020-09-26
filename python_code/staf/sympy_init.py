try:
    from sympy import lambdify, diff, simplify, pretty, solve, symbols
    from sympy.parsing.sympy_parser import parse_expr
    x, y = symbols('x y')
except ModuleNotFoundError:
    try:
        import os
        os.system('pip install sympy')
        os.system('pip3 install sympy')
        from sympy import Symbol, lambdify, diff, simplify
        from sympy.parsing.sympy_parser import parse_expr
        x = Symbol('x')
    except Exception as error:
        input(str(error))
