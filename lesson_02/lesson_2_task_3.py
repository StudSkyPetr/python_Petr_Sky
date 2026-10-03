from math import ceil

def square(gran):
    kvadrat = gran * gran
    return kvadrat

dlina = float(input("Введите длину стороны квадрата в сантиметрах "))
s_result = square(dlina)
print(f"Площадь (округленная вверх) квадрата со стороной  {dlina} -  {ceil(s_result)} см")
