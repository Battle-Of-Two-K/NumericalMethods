# NumericalMethods
## Численные методы
Основные идеи:
1. Минимум внешних модулей, без внешних модулей для численных методов
1. Максимум комментариев в коде
1. Максимум русского языка
### Инструкция
Изучить Python можно решая простые задачи, желательно на [сайте с автоматической проверкой решений](https://informatics.mccme.ru/)\
Рекомендации касательно ПО для работы с Python описаны в разделе [для участия](#Для-участия)
#### Для запуска
1. Установить интерпретатор Python 3 и выше, который можно скачать с [официального сайта](https://www.python.org/downloads/).
Рекомендую во время установки поставить галочку в пункте "Add to PATH", в самом начале
1. Скачать архив с этого сайта (зеленая кнопка code -> download zip), распаковать в любое место папку из архива.
1. В папке есть файлы "task%.py" - решения соответствующих заданий. Измените любым текстовым редактором (хоть блокнотом)
числа внутри (внутри подписано что и где писать)
1. Сохраните, закройте редактор и запустите как любую другую программу, двойным кликом (если не вышло, то открыть с помощью -> 
найдите python.exe на компъютере. Обычно он прячется в C:\Users\\<User>\AppData\Local\Programs\Python\Python37-32)
1. Готово! А те, кто хочет сам что-то написать, используя модули этого репозитория должны создать файл свое_название.py
рядом с папкой python_code, в файле первой строкой импортировать все необходимое: "from python_code.main import *", а дальше
используйте документацию ниже 
#### Регулярные обновления (НЕ автоматические)
При обнаружении ошибок, автор **старается** их исправлять в следующем обновлении. \
Обновлять программу можно каждый раз скачивая новый архив, полностью заменять его содержимым свою версию.\
Для автоматизации процесса можно использовать Git. Краткая инструкция к обновлению с использованием Git:\
1. Установить Git-клиент на выбор (разница в интерфейсе пользователя):
    - [Git](https://git-scm.com/downloads) (Для Git Bash инструкции более полные)
    - [SublimeMerge](https://www.sublimemerge.com/)
    - [Github Desktop](https://desktop.github.com/)\
    P.S. Для некоторых клиентов иногда требуется сам Git
2. Клонировать репозиторий
    - Консольный интерфейс - открыть Bash (ПКМ в папке -> Git Bash Here)\
    выполнить команду: git clone https://github.com/simensgreen/NumericalMethods\
    (папка будет загружена в директорию, в которой открыт bash (консоль))
    - В графическом интерфейсе найти аналог "git clone" и указать ссылку на репозиторий (скопировать из браузера)
3. Обновить
    - Консольный интерфейс - открыть Bash в папке с программой (нужно зайти в папку) (ПКМ в папке -> Git Bash Here)\
    выполнить команду: git pull
    - В графическом интерфейсе найти аналог "git pull" (зачастую это стрелочка вниз)
P.S. На этапе могут возникать ошибки гита, они могут быть связаны с тем, что вы изменили файлы и гит защищает вас от потери
данных. Если вас это не волнует, можете исправить данные до исходного состояния или применить команду git stash до git pull.
Подробнее про [git stash](http://stepansuvorov.com/blog/2012/11/git-stash-%D1%8D%D1%82%D0%BE-%D1%82%D0%BE-%D1%87%D1%82%D0%BE-%D1%8F-%D0%B8%D1%81%D0%BA%D0%B0%D0%BB/)
(правильное применение команд гита может сохранить ваши данные)
#### Для участия
1. Зарегистрироваться на [GitHub](http://github.com)
1. Написать свою почту (по которой регистрировался) в [личку](https://vk.com/simens_green) чтобы я добавил к разработчикам.
1. Если решил влезть в код, то рекомендую это делать с помощью [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/) или 
([SublimeText3](https://www.sublimetext.com/3) или [Spyder](https://www.spyder-ide.org/) или [Atom](https://atom.io/)) + 
[Kite](https://www.kite.com/)
1. Для более удобного использования GitHub лучше установить [Git](https://ru.wikipedia.org/wiki/Git#:~:text=Git%20(%D0%BF%D1%80%D0%BE%D0%B8%D0%B7%D0%BD%D0%BE%D1%81%D0%B8%D1%82%D1%81%D1%8F%20%C2%AB%D0%B3%D0%B8%D1%82%C2%BB),%D0%B4%D0%B5%D0%BD%D1%8C%20%D0%B5%D0%B3%D0%BE%20%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B8%D0%B2%D0%B0%D0%B5%D1%82%20%D0%94%D0%B6%D1%83%D0%BD%D0%B8%D0%BE%20%D0%A5%D0%B0%D0%BC%D0%B0%D0%BD%D0%BE.)-клиент, например сам 
[Git](https://git-scm.com/downloads) или [SublimeMerge](https://www.sublimemerge.com/) или [Github Desktop](https://desktop.github.com/)
### Структура
1. В папке [python_code](https://github.com/simensgreen/NumericalMethods/tree/master/python_code) 
лежит основной код программы (в случае желания редактировать - в _master_ **не пушить**!)
1. В папке [block diagrams](https://github.com/simensgreen/NumericalMethods/tree/master/block%20diagrams) должны лежать 
картинки с блок-схемами алгоритмов.
1. В папке [text descriptions](https://github.com/simensgreen/NumericalMethods/tree/master/text%20descriptions) должны 
лежать текстовые описания алгоритмов. \
P.S. в каждой папке по две папки - для разделения матриц и интергалов. В будущем структура может быть изменена.
# Документация
(Для продвинутого использования)
1. Класс [Matrix](#Класс-Matrix)
1. [Определитель](#Определитель)
1. [Нахождение корней уравнений](#Нахождение-корней-уравнений)
    - [Многочлен](#Многочлен)
        - [Метод Лобачевского](#Метод-Лобачевского)
        - [Метод дихотомии](#Метод-дихотомии)
1. [Методы решений СЛАУ](#Методы-решений-СЛАУ)
    - [Метод Гаусса](#Метод-Гаусса)
    - [Метод простых итераций](#Метод-простых-итераций)
    - [Метод Зейделя](#Метод-Зейделя)
    - [Метод прогонки](#Метод-прогонки)
    - [Метод Крамера](#Метод-Крамера)
1. [Решения второй задачи линейной алгебры](#Решения-второй-задачи-линейной-алгебры)
    - [Степенной метод вычисления спектрального радиуса](#Степенной-метод-вычисления-спектрального-радиуса)
    - [Метод вращений Якоби для симметричной матрицы](Метод-вращений-Якоби-для-симметричной-матрицы)
### Класс Matrix
Класс Matrix - общий класс для матриц любого порядка. В нем объявлено большинство методов для работы с матрицами/
Нумерация строк и столбцов начинается с 0.
1. [Атрибуты и свойства (@property)](#Атрибуты-и-свойства):
    * [complements](#complements) (Matrix) - матрица алгебраических дополнений
    * [T](#T) (Matrix) - транспонированная матрица
    * [is_dominant](#is_dominant) (bool) - проверка на преобладающую главную диагональ
    * [is_square](#is_square) (bool) - является ли матрица квадратной
    * [is_symmetrical](#is_symmetrical) (bool) - является лиматрица симметричной
    * [is_triple_diagonal](#is_triple_diagonal)(bool)  - является ли матрица трехдиагональной
    * [max_len_num](#max_len_num) (int) - вычисление максимальной длины строкового отображения значений матрицы
    * [rows](#rows) (int) - количество строк матрицы
    * [columns](#columns) (int) - количество столбцов матрицы
    * [norma_1](#norma_1) (float, int) - первая норма матрицы
    * [norma_2](#norma_2) (float, int) - вторая норма матрицы
    * [norma_3](#norma_3) (float, int) - третья норма матрицы
    * [matrix](#matrix) (list[list]) - двумерный список, содержащий саму матрицу
    * [size](#size) (tuple[int]) - размер матрицы
    * [vector_to_list](#vector_to_list) (list) - Преобразует матрицу (вектор) в список
    * [vector_norma_1](#vector_norm_1) (float, int) - первая норма вектора
    * [vector_norma_2](#vector_norm_2) (float, int) - вторая норма вектора
    * [vector_norma_3](#vector_norm_3) (float, int) - Евклидова (третья) норма вектора
2. [Методы](#Методы)
    * [minor](#minor) (Matrix) - нахождение минора матрицы
    * [swap_rows](#swap_rows) (Matrix) - меняет строки местами
    * [swap_columns](#swap_columns) (Matrix) - меняет столбцы местами
    * [copy](#copy) (Matrix) - возвращает глубокую копию матрицы
    * [triangulate](#triangulate) (Matrix) - возвращает триангулированную матрицу (верх)
    * [triangulate_to_ones](#triangulate_to_ones) (Matrix) - возвращает триангулированную матрицу (верх) с единицами в диагонали
    * [search_for_max_num_count](#search_for_max_num_count) (int) - ищет строку с максимальным количеством входжений указанного числа
    * [pop_column](#pop_column) (list) - удаляет указанный столбец и возвращает его в виде списка (меняет исходную)
    * [pop_row](#pop_row) (list) - удаляет указанную строку и возвращает ее в виде списка (меняет исходную)
    * [to_pretty_string](#to_pretty_string) (str) - создает таблицу со значениями
    * [console_display](#console_display) (None) - печатает таблицу матрицы в консоль
    * [dump_to_file](#dump_to_file) (None) - сохраняет матрицу в файл без потери точности
    * [append_row](#append_row) (None) - дописывает строку снизу матрицы (меняет исходную)
    * [autofill](#autofill) (None) - автоматическое заполнение матрицы (меняет исходную)
    * [append_column](#append_column) (None) - дописывает столбец справа (меняет исходную)
    * [load_from_file](#load_from_file) (None) - загружает матрицу из файла без потери точности (меняет исходную)
    * [write_to_file](#write_to_file) (None) - записывает таблицу в файл (с потерей точности)
    * [read_from_file](#read_from_file) (None) - читает таблицу из текстового файла (меняет исходную)
    * [vector_scalar_mul](#vector_scalar_mul) (float, int) - скалярное произведение векторов
    * [insert_row](#insert_row) (None) - вставляет строку в исходную матрицу
    * [insert_column](#insert_column) (None) - вставляет столбец в исходную матрицу
    * [wrap](#wrap) (Matrix) - оборачивает двумерный список в матрицу
    * [vector_get_norm_3_vector](#vector_get_norm_3_vector) (Matrix) - создает нормированный вектор указанного размера
3. Перегруженные и переопределенные методы
    * \_\_getitem__ - получение по индексу или срезу
    * \_\_setitem__ - присвоение по индексу
    * \_\_str__ - преобразование в строковый тип
    * \_\_add__ - оператор сложения (+)
    * \_\_mul__ - оператор умножения (*)
    * \_\_neg__ - унарный минус (-)
    * \_\_truediv__ - деление с плавающей точкой (/)
    * \_\_invert__ - инверсия (~) (Возвращает обратную матрицу)
    * \_\_eq__ - сравнение (==)
    * \_\_hash__ - хэш
### Методы
#### minor
Принимает на вход номер строки и столбца элемента, возвращает матрицу без этой строки и столбца.\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill('sequence')
matrix.console_display()
matrix.minor(1, 1).console_display()
# Ожидаемый выход:
# Матрица (3, 3)
#  ___________ 
# | 1 | 2 | 3 |
# |___|___|___|
# | 4 | 5 | 6 |
# |___|___|___|
# | 7 | 8 | 9 |
# |___|___|___|
# 
# Матрица (2, 2)
#  _______ 
# | 1 | 3 |
# |___|___|
# | 7 | 9 |
# |___|___|
```
#### swap_rows
Принимает на вход номера строк, меняет их местами и возвращает измененную матрицу.\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill('sequence')
matrix.console_display()
matrix.swap_rows(0, 2).console_display()
# Ожидаемый выход:
# Матрица (3, 3)
#  ___________ 
# | 1 | 2 | 3 |
# |___|___|___|
# | 4 | 5 | 6 |
# |___|___|___|
# | 7 | 8 | 9 |
# |___|___|___|
# 
# Матрица (3, 3)
#  ___________ 
# | 7 | 8 | 9 |
# |___|___|___|
# | 4 | 5 | 6 |
# |___|___|___|
# | 1 | 2 | 3 |
# |___|___|___|
```
#### swap_columns
Принимает на вход номера столбцов, меняет их местами и возвращает измененную матрицу.\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill('sequence')
matrix.console_display()
matrix.swap_columns(0, 2).console_display()
# Ожидаемый выход:
# Матрица (3, 3)
#  ___________ 
# | 1 | 2 | 3 |
# |___|___|___|
# | 4 | 5 | 6 |
# |___|___|___|
# | 7 | 8 | 9 |
# |___|___|___|
# 
# Матрица (3, 3)
#  ___________ 
# | 3 | 2 | 1 |
# |___|___|___|
# | 6 | 5 | 4 |
# |___|___|___|
# | 9 | 8 | 7 |
# |___|___|___|
```
#### triangulate
Возвращает триангулированную матрицу\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill()
matrix.console_display()
matrix.triangulate().console_display()
# Ожидаемый выход:
#   Матрица (3, 3) 
#  _________________ 
# |  -3 | -10 |  2  |
# |_____|_____|_____|
# |  9  |  -1 |  9  |
# |_____|_____|_____|
# |  -7 |  -8 |  1  |
# |_____|_____|_____|
# 
#             Матрица (3, 3)            
#  ______________________________________ 
# |     -3     |    -10     |     2      |
# |____________|____________|____________|
# |    0.0     |   -31.0    |    15.0    |
# |____________|____________|____________|
# |    0.0     |    0.0     | 3.75268817 |
# |____________|____________|____________|
```
#### copy
Возвращает глубокую копию матрицы\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill('sequence')
new_matrix = matrix.copy()
```
#### triangulate_to_ones
Возвращает триангулированную матрицу с единицами в главной диагонали\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill()
matrix.console_display()
matrix.triangulate_to_ones().console_display()
# Ожидаемый выход:
# Матрица (3, 3)
#  ______________ 
# | 4  | -4 | -6 |
# |____|____|____|
# | 6  | -2 | -2 |
# |____|____|____|
# | -6 | 0  | 7  |
# |____|____|____|
# 
#    Матрица (3, 3)   
#  ____________________ 
# | 1.0  | -1.0 | -1.5 |
# |______|______|______|
# | 0.0  | 1.0  | 1.75 |
# |______|______|______|
# | 0.0  | 0.0  | 1.0  |
# |______|______|______|

```
#### search_for_max_num_count
Принимает на вход значение, возвращает номер строки с максимальным количеством вхождений этого значения.\
По умолчанию num=0
Пример использования:
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill()
matrix.console_display()
print(matrix.search_for_max_num_count(1))
# Ожидаемый выход:
# Матрица (3, 3)
#  ______________ 
# | -1 | -4 | -5 |
# |____|____|____|
# | -9 | -7 | -6 |
# |____|____|____|
# | 3  | 8  | -2 |
# |____|____|____|
# 
# 0
```
#### pop_column
Принимает на вход номер столбца, удаляет его из исходной матрицы и возвращает столбец в виде списка\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill('sequence')
column = matrix.pop_column(1)
matrix.console_display()
print(column)
# Ожидаемый выход:
# Матрица (3, 2)
#  _______ 
# | 1 | 3 |
# |___|___|
# | 4 | 6 |
# |___|___|
# | 7 | 9 |
# |___|___|
# 
# [2, 5, 8]
```
#### pop_row
Принимает на вход номер строки, удаляет ее из исходной матрицы и возвращает строку в виде списка\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill('sequence')
column = matrix.pop_row(1)
matrix.console_display()
print(column)
# Ожидаемый выход:
# Матрица (2, 3)
#  ___________ 
# | 1 | 2 | 3 |
# |___|___|___|
# | 7 | 8 | 9 |
# |___|___|___|
# 
# [4, 5, 6]
```
#### to_pretty_string
Возвращает отформатрированную в виде таблицы матрицу\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill('sequence')
print(matrix.to_pretty_string())
# Ожидаемый выход:
#  ___________ 
# | 1 | 2 | 3 |
# |___|___|___|
# | 4 | 5 | 6 |
# |___|___|___|
# | 7 | 8 | 9 |
# |___|___|___|
```
#### console_display
Печатает в консоль отформатрированную в виде таблицы матрицу\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill()
matrix.console_display()
# Ожидаемый выход:
# Матрица (3, 3)
#  ______________ 
# | 5  | -4 | 1  |
# |____|____|____|
# | 5  | 5  | 6  |
# |____|____|____|
# | 0  | -2 | -4 |
# |____|____|____|
```
#### dump_to_file
Сохраняет матрицу в файл без потери точности\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill('sequence')
matrix.dump_to_file('file')
new_matrix = Matrix(3)
new_matrix.load_from_file('file')
new_matrix.console_display()
# Ожидаемый выход:
# Матрица (3, 3)
#  ___________ 
# | 1 | 2 | 3 |
# |___|___|___|
# | 4 | 5 | 6 |
# |___|___|___|
# | 7 | 8 | 9 |
# |___|___|___|
```
#### append_row
Принимает список и присоединяет его снизу к исходной матрице, как новую строку\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(2)
matrix.autofill('sequence')
matrix.console_display()
matrix.append_row([5, 6])
matrix.console_display()
# Ожидаемый выход:
# Матрица (2, 2)
#  _______ 
# | 1 | 2 |
# |___|___|
# | 3 | 4 |
# |___|___|
# 
# Матрица (3, 2)
#  _______ 
# | 1 | 2 |
# |___|___|
# | 3 | 4 |
# |___|___|
# | 5 | 6 |
# |___|___|
```
#### autofill
Автоматическое заполнение матрицы.
1. Режимы:
    * 'random' - случайные числа в диапазоне options если в options int, то целые, иначе - не целые (по умолчанию (-10, 10))
    * 'ones' - заполняет единицами
    * 'diagonal_ones' - приводит матрицу к единичной
    * 'sequence' - матрица, заполненная числами от 1 до Matrix.rows * Matrix.columns
    * 'H_grid' - прямая сетка значений (по умолчанию (1, 0, 2))
    * 'X_grid' - косая сетка значений (по умолчанию (1, 0)
    * 'dominant' - матрица с доминантной диагональю, options как у 'random'
    * 'exchange' - обменная матрица
    * 'triple_diagonal' - Трёхдиагональная матрица, options как у 'random'"""
По умолчанию mode='random', options=(-10, 10)\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(4)
matrix.autofill('sequence')
matrix.console_display()
matrix.autofill('random', options=(-10., 10))
matrix.console_display()
matrix.autofill('dominant')
matrix.console_display()
# Ожидаемый выход:
#    Матрица (4, 4)  
#  ___________________ 
# | 1  | 2  | 3  | 4  |
# |____|____|____|____|
# | 5  | 6  | 7  | 8  |
# |____|____|____|____|
# | 9  | 10 | 11 | 12 |
# |____|____|____|____|
# | 13 | 14 | 15 | 16 |
# |____|____|____|____|
# 
#                      Матрица (4, 4)                    
#  _______________________________________________________ 
# | -0.20354909 | -5.49033619 |  0.40014911 |  2.54649543 |
# |_____________|_____________|_____________|_____________|
# | -3.62709774 |  7.03031092 |  3.5894645  | -4.71427915 |
# |_____________|_____________|_____________|_____________|
# |  6.10161374 |  1.83048589 |  1.91927223 |  2.3427441  |
# |_____________|_____________|_____________|_____________|
# |  8.7610529  | -5.64686201 |  5.31600698 |  5.75095304 |
# |_____________|_____________|_____________|_____________|
# 
#      Матрица (4, 4)    
#  _______________________ 
# | -17 |  1  |  -7 |  -4 |
# |_____|_____|_____|_____|
# |  5  | -23 |  8  |  -8 |
# |_____|_____|_____|_____|
# |  0  |  3  | -19 |  7  |
# |_____|_____|_____|_____|
# |  2  |  -3 |  6  | -21 |
# |_____|_____|_____|_____|
```
#### append_column
Принимает на вход список и присоединяет его к исходной матрице справа как новый столбец\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(3, 2)
matrix.autofill('sequence')
matrix.console_display()
matrix.append_column([0, 0, 0])
matrix.console_display()
# Ожидаемый выход:
# Матрица (3, 2)
#  _______ 
# | 1 | 2 |
# |___|___|
# | 3 | 4 |
# |___|___|
# | 5 | 6 |
# |___|___|
# 
# Матрица (3, 3)
#  ___________ 
# | 1 | 2 | 0 |
# |___|___|___|
# | 3 | 4 | 0 |
# |___|___|___|
# | 5 | 6 | 0 |
# |___|___|___|
```
#### load_from_file
Загружает матрицу из файла (поддерживаются только файлы, сгенерированные dump_to_file)\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill('sequence')
matrix.dump_to_file('file')
new_matrix = Matrix(3)
new_matrix.load_from_file('file')
new_matrix.console_display()
# Ожидаемый выход:
# Матрица (3, 3)
#  ___________ 
# | 1 | 2 | 3 |
# |___|___|___|
# | 4 | 5 | 6 |
# |___|___|___|
# | 7 | 8 | 9 |
# |___|___|___|
```
#### write_to_file
Записывает в файл таблицу, полученную методом to_pretty_string\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(3)
matrix.write_to_file('file')
new_matrix = Matrix(3)
matrix.read_from_file('file')
matrix.console_display()
# Ожидаемый выход:
# Матрица (3, 3)
#  ___________ 
# | 1 | 2 | 3 |
# |___|___|___|
# | 4 | 5 | 6 |
# |___|___|___|
# | 7 | 8 | 9 |
# |___|___|___|
```
#### read_from_file
Читает из файла таблицу (должна соответствовать той, что генерируется write_to_file)\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(3)
matrix.write_to_file('file')
new_matrix = Matrix(3)
matrix.read_from_file('file')
matrix.console_display()
# Ожидаемый выход:
# Матрица (3, 3)
#  ___________ 
# | 1 | 2 | 3 |
# |___|___|___|
# | 4 | 5 | 6 |
# |___|___|___|
# | 7 | 8 | 9 |
# |___|___|___|
```
### Атрибуты и свойства
#### complements
Матрица алгебраических дополнений к исходной матрице
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill()
matrix.console_display()
matrix.complements.console_display()
# Ожидаемый выход:
# Матрица (3, 3)
#  ______________ 
# | 7  | -7 | -5 |
# |____|____|____|
# | 0  | 9  | 0  |
# |____|____|____|
# | 3  | 5  | -4 |
# |____|____|____|
# 
#   Матрица (3, 3) 
#  _________________ 
# | -36 |  0  | -27 |
# |_____|_____|_____|
# | -53 | -13 | -56 |
# |_____|_____|_____|
# |  45 |  0  |  63 |
# |_____|_____|_____|
```
#### T
Транспонированная матрица
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill('sequence')
matrix.console_display()
matrix.T.console_display()
# Ожидаемый выход:
# Матрица (3, 3)
#  ___________ 
# | 1 | 2 | 3 |
# |___|___|___|
# | 4 | 5 | 6 |
# |___|___|___|
# | 7 | 8 | 9 |
# |___|___|___|
# 
# Матрица (3, 3)
#  ___________ 
# | 1 | 4 | 7 |
# |___|___|___|
# | 2 | 5 | 8 |
# |___|___|___|
# | 3 | 6 | 9 |
# |___|___|___|
```
#### is_dominant
Проверка на преобладающую главную диагональ
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill()
matrix.console_display()
matrix_2 = Matrix(3)
matrix_2.autofill('dominant')
matrix_2.console_display()
print(matrix.is_dominant, matrix_2.is_dominant)
# Ожидаемый выход:
# Матрица (3, 3)
#  ______________ 
# | 3  | 5  | -4 |
# |____|____|____|
# | 4  | -1 | 5  |
# |____|____|____|
# | 6  | 3  | -3 |
# |____|____|____|
# 
#   Матрица (3, 3) 
#  _________________ 
# | -17 |  -3 |  9  |
# |_____|_____|_____|
# |  8  | -14 |  3  |
# |_____|_____|_____|
# |  4  |  -2 | -10 |
# |_____|_____|_____|
# 
# False True
```
#### is_square
Является ли матрица квадратной
```python
from python_code.main import *
matrix = Matrix(3)
matrix_2 = Matrix(3, 4)
print(matrix.is_square, matrix_2.is_square)
# Ожидаемый выход:
# True False
```
#### is_triple_diagonal
Является ли матрица трехдиагональной (нужно, например, для метода прогонки)
```python
from python_code.main import *
matrix = Matrix(4)
matrix.autofill()
matrix.console_display()
matrix_2 = Matrix(4)
matrix_2.autofill('triple_diagonal')
matrix_2.console_display()
print(matrix.is_triple_diagonal, matrix_2.is_triple_diagonal)
# Ожидаемый выход:
#      Матрица (4, 4)    
#  _______________________ 
# |  10 |  -9 |  -4 | -10 |
# |_____|_____|_____|_____|
# |  5  |  -6 |  -1 |  -4 |
# |_____|_____|_____|_____|
# |  -6 |  8  |  -7 |  -6 |
# |_____|_____|_____|_____|
# |  1  |  -1 |  6  |  -7 |
# |_____|_____|_____|_____|
# 
#    Матрица (4, 4)  
#  ___________________ 
# | -7 | -9 | 0  | 0  |
# |____|____|____|____|
# | 10 | -4 | -6 | 0  |
# |____|____|____|____|
# | 0  | 0  | 8  | -2 |
# |____|____|____|____|
# | 0  | 0  | 9  | 8  |
# |____|____|____|____|
# 
# False True
```
#### max_len_num
Вычисление максимальной длины строкового отображения значений матрицы
Преобразует каждое значение в строку (набор символов), считает сколько получилось и выдает максимальное значение (нужно для to_pretty_string)
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill(options=(-10., 10))
matrix.console_display()
print(matrix.max_len_num)
# Ожидаемый выход:
#               Матрица (3, 3)             
#  _________________________________________ 
# | -2.70573464 |  6.45341549 | -6.73833746 |
# |_____________|_____________|_____________|
# |  3.49760234 | -1.24910919 |  7.72165818 |
# |_____________|_____________|_____________|
# |  4.0763576  | -9.63916566 |  -4.6361087 |
# |_____________|_____________|_____________|
# 
# 11
```
#### rows
Количество строк матрицы
```python
from python_code.main import *
matrix = Matrix(3)
print(matrix.rows, matrix.columns)
# Ожидаемый выход:
# 3 3
```
#### columns
Количество столбцов матрицы
```python
from python_code.main import *
matrix = Matrix(3)
print(matrix.rows, matrix.columns)
# Ожидаемый выход:
# 3 3
```
#### norma_1
Первая норма матрицы
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill()
matrix.console_display()
print(matrix.norma_1)
# Ожидаемый выход:
# Матрица (3, 3)
#  ______________ 
# | 7  | -4 | 8  |
# |____|____|____|
# | 0  | -7 | -4 |
# |____|____|____|
# | -3 | 5  | 0  |
# |____|____|____|
# 
# 19
```
#### norma_2
Вторая норма матрицы
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill()
matrix.console_display()
print(matrix.norma_2)
# Ожидаемый выход:
# Матрица (3, 3)
#  ______________ 
# | 7  | -9 | 2  |
# |____|____|____|
# | 6  | 3  | 8  |
# |____|____|____|
# | -9 | -7 | 1  |
# |____|____|____|
# 
# 22
```
#### matrix
(list[list]) - двумерный список, содержащий саму матрицу
```python
from python_code.main import *
matrix = Matrix(3)
matrix.autofill('sequence')
print(matrix.matrix)
# Ожидаемый выход:
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
#### size
(tuple[int]) - размер матрицы
```python
from python_code.main import *
matrix = Matrix(5, 10)
print(matrix.size)
# Ожидаемый выход:
# (5, 10)
```
## Определитель
Описано 3 метода нахождения определителя в модуле determinant, но функция det из main и auto_det из determinant выберут самый быстрый способ\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(5)
print(det(matrix))
```
## Нахождение корней уравнений
### Многочлен
#### Метод Лобачевского
Метод Лобачевского не описан в [методичке](https://github.com/simensgreen/NumericalMethods/blob/master/text%20descriptions/MA_Cherkasov_Kurs_chisl_metodov_2020_03_22.pdf)\
Пример использования:
```python
from python_code import *
polynom = [1, -5, 6]
correct_roots = [3, 2]
# Для получения промежуточной информации нужно указать уровень детализации, где 1 - полная детализация, 3 - только ответ
decision = methods.equation.polynomial.lobachevsky_method(polynom)
solution = []
for step in decision:
    solution = step.get('Решение')
print(solution)
```
#### Метод дихотомии
Метод дихотомии описан в [методичке](https://github.com/simensgreen/NumericalMethods/blob/master/text%20descriptions/MA_Cherkasov_Kurs_chisl_metodov_2020_03_22.pdf)
в пункте 5.1 Метод половинного деления (дихотомии, бисекций), страница 39.\
Пример использования:
```python
from python_code.methods.equation import dichotomy


def f(x):
    return x ** 2 - 2


section = (0, 8)
decision = dichotomy(f, section)
solution = None
for step in decision:
    solution = step.get('Решение')
print(solution)
# Для получения промежуточной информации нужно указать уровень детализации, где 1 - полная детализация, 3 - только ответ
# accuracy_order - необходимый порядок точности, level_of_details - уровень детализации
decision = dichotomy(f, section, accuracy_order=8, level_of_details=2)
```
## Методы решений СЛАУ
### Метод Гаусса
Метод Гаусса описан в [методичке](https://github.com/simensgreen/NumericalMethods/blob/master/text%20descriptions/MA_Cherkasov_Kurs_chisl_metodov_2020_03_22.pdf)
в пункте 1.1 Метод Гаусса решения СЛАУ, страница 7.\
Пример использования:
```python
from python_code.main import *
matrix = Matrix([[20, 4, -8], [-3, 15, 5], [6, 3, -18]])
free_column = [1, -2, 3]
print(gauss.gauss_method(matrix, free_column))
# Для вывода промежуточной информации, флаг print_middle_values нужно поставить в True, как ниже
print(gauss.gauss_method(matrix, free_column, print_middle_values=True))
```
### Метод простых итераций
Метод простых итераций описан в [методичке](https://github.com/simensgreen/NumericalMethods/blob/master/text%20descriptions/MA_Cherkasov_Kurs_chisl_metodov_2020_03_22.pdf)
в пункте 2.1 Метод простых итераций решения СЛАУ, страница 22.
Данная реализация возвращает итерируемый объект, а не решение\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(4)
matrix.autofill('dominant')
free_column = [1, -2, 3, 5]
# iterations=8 означает, что нужно остановиться после 8 итерации
decision = iterations.simple_iterations(matrix, free_column, iterations=8)
# Для получения решения необходимо пропустить все шаги
solution = None
for step in decision:
    solution = step.get("Решение")
print(solution)
# Для получения промежуточной информации нужно указать уровень детализации, где 1 - полная детализация, 3 - только ответ
# await_e=10 ** (-5) означает, что цикл нужно продолжать, пока Эпсилон не станет ниже десять в минус пятой степени
decision = iterations.simple_iterations(matrix, free_column, await_e=10 ** (-5), level_of_detail=2)
```
### Метод Зейделя
Метод Зейделя описан в [методичке](https://github.com/simensgreen/NumericalMethods/blob/master/text%20descriptions/MA_Cherkasov_Kurs_chisl_metodov_2020_03_22.pdf)
в пункте 2.2 Метод Зейделя решения СЛАУ, страница 26.
Данная реализация возвращает итерируемый объект, а не решение\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(4)
matrix.autofill('dominant')
free_column = [1, -2, 3, 5]
# iterations=8 означает, что нужно остановиться после 8 итерации
decision = iterations.zeidel_method(matrix, free_column, iterations=8)
# Для получения решения необходимо пропустить все шаги
solution = None
for step in decision:
    solution = step.get("Решение")
print(solution)
# Для получения промежуточной информации нужно указать уровень детализации, где 1 - полная детализация, 3 - только ответ
# await_e=10 ** (-5) означает, что цикл нужно продолжать, пока Эпсилон не станет ниже десять в минус пятой степени
decision = iterations.zeidel_method(matrix, free_column, await_e=10 ** (-5), level_of_detail=2)
```
### Метод прогонки
Метод прогонки описан в [методичке](https://github.com/simensgreen/NumericalMethods/blob/master/text%20descriptions/MA_Cherkasov_Kurs_chisl_metodov_2020_03_22.pdf)
в пункте 1.6 Решение трёхдиагональной СЛАУ методом прогонки, страница 18.\
Пример использования:
```python
from python_code.main import *
matrix = Matrix(4)
matrix.autofill('triple_diagonal')
free_column = [1, -2, 3, 5]
decision = iterations.triple_diagonal(matrix, free_column)
# Для получения решения необходимо пропустить все шаги
solution = None
for step in decision:
    solution = step.get("Решение")
print(solution)
# Для получения промежуточной информации нужно указать уровень детализации, где 1 - полная детализация, 3 - только ответ
# await_e=10 ** (-5) означает, что цикл нужно продолжать, пока Эпсилон не станет ниже десять в минус пятой степени
decision = iterations.triple_diagonal(matrix, free_column, level_of_detail=2)
```
### Метод Крамера
Метод Крамера не описан в [методичке](https://github.com/simensgreen/NumericalMethods/blob/master/text%20descriptions/MA_Cherkasov_Kurs_chisl_metodov_2020_03_22.pdf).\
Пример использования:
```python
from python_code import *
matrix = Matrix([[2, 1, 1], [1, -1, 0], [3, -1, 2]])
free = [2, -2, 2]
decision = methods.matrix.kramer_method(matrix, free)
solution = None
for step in decision:
    print(step)
    solution = step.get("Решение")
# Для получения промежуточной информации нужно указать уровень детализации, где 1 - полная детализация, 3 - только ответ
decision = methods.matrix.kramer_method(matrix, free, level_of_detail=2)
```

## Решения второй задачи линейной алгебры
### Степенной метод вычисления спектрального радиуса
Степенной метод вычисления спектрального радиуса описан в [методичке](https://github.com/simensgreen/NumericalMethods/blob/master/text%20descriptions/MA_Cherkasov_Kurs_chisl_metodov_2020_03_22.pdf)
в пункте 3.1 Степенной метод вычисления спектрального радиуса, страница 28.\
Пример использования:
```python
from python_code import *
matrix = Matrix([[-12, 4, 8], [4, 11, -6], [8, -6, 2]])
decision = methods.matrix.power_method(matrix, iterations=21)
solution = None
for step in decision:
    solution = step.get("Решение")
print(solution)
# Для получения промежуточной информации нужно указать уровень детализации, где 1 - полная детализация, 3 - только ответ
# await_d=10 ** (-5) означает, что цикл нужно продолжать, пока Дельта не станет ниже десять в минус пятой степени
decision = methods.matrix.power_method(matrix, level_of_detail=2, await_d=10 ** (-5))
```
### Метод вращений Якоби для симметричной матрицы
Метод вращений Якоби для симметричной матрицы описан в [методичке](https://github.com/simensgreen/NumericalMethods/blob/master/text%20descriptions/MA_Cherkasov_Kurs_chisl_metodov_2020_03_22.pdf)
в пункте 3.2 Метод вращений Якоби для симметричной матрицы, страница 33.\
Пример использования:
```python
from python_code import *
matrix = Matrix([[17, 1, 1], [1, 17, 2], [1, 2, 4]])
decision = method_rot_yakobi(matrix, iterations=8)
solution = None
for step in decision:
    solution = step.get("Решение")
print(solution)
# Для получения промежуточной информации нужно указать уровень детализации, где 1 - полная детализация, 3 - только ответ
decision = methods.matrix.power_method(matrix, level_of_detail=2)
```
