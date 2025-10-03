def my_adder(a, b, c):
    return a + b + c


def my_thermo_stat(temp, desired_temp):
    if temp <= desired_temp - 5:
        return "Heat"
    elif temp >= desired_temp + 5:
        return "AC"
    else:
        return "off"


def have_digits(s):
    for c in s:
        if c.isdigit():
            return 1
    return 0


def area_of_rectangle(width, height):
    return width * height


def perimeter_of_rectangle(width, height):
    return 2 * (width + height)
