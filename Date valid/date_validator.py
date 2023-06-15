def is_leap_year(year):
    # Проверяем, является ли год високосным  
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
    return False

def is_valid_date(date_str):
    # Разделяем строку с датой на день, месяц и год
    day, month, year = map(int, date_str.split('.'))

    # Проверяем год на високосность
    leap_year = is_leap_year(year)

    # Выводим информацию о високосном годе
    if leap_year:
        print(f"{year} год является високосным")
    else:
        print(f"{year} год не является високосным")

    # Проверяем валидность даты
    if year >= 1 and year <= 9999:
        if month >= 1 and month <= 12:
            if month == 2:  # Февраль
                if leap_year and day >= 1 and day <= 29:
                    return True
                elif not leap_year and day >= 1 and day <= 28:
                    return True
                else:
                    return False
            elif month in [4, 6, 9, 11]:  # Апрель, Июнь, Сентябрь, Ноябрь
                if day >= 1 and day <= 30:
                    return True
                else:
                    return False
            else:  # Остальные месяцы с 31 днем
                if day >= 1 and day <= 31:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False
