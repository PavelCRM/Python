from date_validator import is_valid_date

date = input("Введите дату в формате DD.MM.YYYY: ")   

valid = is_valid_date(date)

if valid:
    print("Дата существует")
else:
    print("Дата невозможна")
  