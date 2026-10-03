def month_to_season(month):
    year_s = ["<Весна>", "<Лето>", "<Осень>", "<Зима>"]
    if month == 0 or month > 12:
        print ("Пожалуйста, вводите номер месяца аккуратнее: в году 12 месяцев!")
    elif month > 0 and month < 3 or month == 12:
        return year_s[3]
    elif month > 2 and month < 6:
        return year_s[0]
    elif month > 5 and month < 9:
        return year_s[1]
    elif month > 8 and month < 12:
        return year_s[2]

mnth = int(input("Введите номер месяца (от 1 до 12) для определения к какому сезону он отностися -  "))
season = month_to_season(mnth)
print(f"Месяц с номером  -  {mnth} Это сезон   {season}")
