def iterations(function, gfunction, gdiff, section):
    def calc_x():
        return gfunction(x0)

    a = min(section)
    b = max(section)
    if gdiff(b) < 1:
        x0 = b
    else:
        x0 = a
    for i in range(10):
        print(i, x0, function(x0), gfunction(x0), gdiff(x0))
        x0 = calc_x()


def f(x):
    return 3 * x ** 3 + 7 * x + 20


def g(x):
    return ((-7 * x - 20) ** (1 / 3)) / 3


def gd(x):
    return 7 / (9 * (-7 * x - 20) ** (2 / 3))

