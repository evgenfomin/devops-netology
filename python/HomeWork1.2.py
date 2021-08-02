import datetime

YourMonth = int(input("ВВедите месяц вашего рождения в формате ММ "))
YourDate = int(input("ВВедите дату вашего рождения в формате DD "))

if YourMonth < 12 or YourDate < 31:
    if (YourMonth == 12 and 21 < YourDate <= 31) or (YourMonth == 1 and 0 < YourDate < 20):
        print ("Вы козерог")
    if (YourMonth == 1 and 20 < YourDate <= 31) or (YourMonth == 2 and 0 < YourDate <= 18):
        print ("Вы водолей")

else:
    print ("не правильно введенная дата")
    exit(0)