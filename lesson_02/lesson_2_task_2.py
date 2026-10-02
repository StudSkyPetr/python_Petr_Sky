def is_year_leap(yea):
    return "Високосный" if yea % 4 == 0 else "Не високосный"

yy = int(input("Введите номер года, который хотите проверить -  "))
Resultat = is_year_leap(yy)

print (f"Год:    {yy} - {Resultat}!")
