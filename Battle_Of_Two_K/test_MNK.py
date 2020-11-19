from sympy import symbols

x, y = symbols('x  y ')

A = -2  # Print
B = -1  # Print

# Считаем колличество шагов
h = 0.2
Go = int((B - A) / h)  # 4
# Go =5
#
K = 1
L = -2
M = 1

Fx = -1 * (x ** 2) - x + 1

# Print
R = 0
S = -3
T = - 4
#
V = 0
W = 3
Z = -4
#
Xx = [A]
for i in range(Go):
    Xx.append(Xx[i] + h)


# Создаем матрицу
def Matrix():
    global Mat1
    # print(Go)
    A = K / h ** 2 - L / 2 / h
    B = (-2) * K / h ** 2 + M
    C = K / h ** 2 + L / 2 / h
    print('b1=', R / h + S)
    print('c1=', R / h)
    print('d1=', Fx.evalf(subs={x: Xx[1]}))
    print('A', A)
    print('B', B)
    print('C', C)
    print('d2=', Fx.evalf(subs={x: Xx[1]}))
    print('d3=', Fx.evalf(subs={x: Xx[2]}))
    print('d4=', Fx.evalf(subs={x: Xx[3]}))
    print('d5=', Fx.evalf(subs={x: Xx[4]}))
    print('a6=', V / h)
    print('b6=', (-V / h - W))
    print('d6=', -Z, '\n')

    Mat1 = [[R / h + S, R / h, 0, 0, 0, 0, T],
            [A, B, C, 0, 0, 0, Fx.evalf(subs={x: Xx[1]})],
            [0, A, B, C, 0, 0, Fx.evalf(subs={x: Xx[2]})],
            [0, 0, A, B, C, 0, Fx.evalf(subs={x: Xx[3]})],
            [0, 0, 0, A, B, C, Fx.evalf(subs={x: Xx[4]})],
            [0, 0, 0, 0, V / h, (-V / h - W), -Z]]


print('-' * 10, 'Расчеты', '-' * 10)

Matrix()

for row in Mat1:
    for list in row:
        print("{:>13.8f}".format(list), end=' ')
    print()

print(f'\n X = {Xx}')


# Progonka
def P():
    Pn = [(-Mat1[0][1] / Mat1[0][0])]
    for i in range(1, len(Mat1) - 1):
        S = (-Mat1[i][i + 1]) / (Mat1[i][i] + Mat1[i][i - 1] * Pn[i - 1])
        Pn.append(S)
    Pn.append(0)
    return Pn


def Q():
    Qn = [(Mat1[0][len(Mat1)] / Mat1[0][0])]
    for i in range(1, len(Mat1)):
        S = (Mat1[i][len(Mat1)] - Mat1[i][i - 1] * Qn[i - 1]) / (Mat1[i][i] + Mat1[i][i - 1] * P()[i - 1])
        Qn.append(S)
    return Qn


def End():
    global Zn
    Zn = [Q()[len(Mat1) - 1]]
    S = Zn[len(Zn) - 1]
    for i in range(len(Mat1) - 2, -1, -1):
        Z = Q()[i] + P()[i] * S
        S = Z
        Zn.append(Z)
    Zn.reverse()
    return Zn


print('\n', 'P', P())
print('\n', 'Q', Q())
print('\n', 'Y=1,2....', '\n', End())

print('-' * 10, 'Ответ', '-' * 10)
print('\nX=', end=' ')
for row in Xx:
    print("{:>13.8f}".format(row), end=' ')
print('\nY=', end=' ')
for row in Zn:
    print("{:>13.8f}".format(row), end=' ')

input()
