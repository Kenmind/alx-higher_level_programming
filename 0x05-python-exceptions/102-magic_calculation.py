#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(a, b):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i

        except Exception:
            result = a + b
            break
    return result
