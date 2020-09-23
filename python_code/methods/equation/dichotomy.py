from math import log10, ceil


def dichotomy(function, section, accuracy_order=8, level_of_details=3):
    def find_center():
        return (right_edge + left_edge) / 2

    def get_section_len():
        return right_edge - left_edge

    def accuracy():
        return ceil(log10(get_section_len()))

    def get_root():
        if accuracy() < 0:
            str_root = str(find_center())
            return float(str_root[:str_root.index('.') + abs(accuracy()) + 1])
        else:
            return None

    answer = {}
    left_edge = min(section)
    right_edge = max(section)
    center = find_center()
    iteration_counter = 0
    while True:
        f_a = function(left_edge)
        f_c = function(center)
        f_b = function(right_edge)
        if level_of_details < 3:
            answer.update({
                'Номер итерации': iteration_counter,
                'a': left_edge,
                'c': center,
                'b': right_edge,
                'f(a)': f_a,
                'f(c)': f_c,
                'f(b)': f_b
            })
            yield answer
            answer.pop('Номер итерации', None)
            answer.pop('a', None)
            answer.pop('c', None)
            answer.pop('b', None)
            answer.pop('f(a)', None)
            answer.pop('f(c)', None)
            answer.pop('f(b)', None)
        if abs(accuracy()) >= accuracy_order:
            if level_of_details < 4:
                answer.update({'Решение': get_root()})
            if level_of_details < 3:
                answer.update({
                    'Последний отрезок': (left_edge, right_edge),
                    'Длина последнего отрезка': get_section_len(),
                    'Середина последнего отрезка': find_center()
                })
            yield answer
            break
        if f_a * f_c < 0:
            right_edge = center
        else:
            left_edge = center
        center = find_center()
        iteration_counter += 1
