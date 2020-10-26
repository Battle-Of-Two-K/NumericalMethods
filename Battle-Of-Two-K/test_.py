s = 0
n = int(input('Введите число: '))

while round(n) != 1:
	n = n / 2
	s += 1

print(s)
