month = int(input("Введите номер месяца: ")) # запросил написать любой номер месяца
day = int(input("Введите день: ")) # запросил написать любой день
if ((month==12 and day >=1 and day <=31) or (month==1 and day >=1 and day <=31)  or (month==2 and day>=1 and day<=29)):
    print("Пора года - зима")
elif ((month==3 and day >=1 and day <=31) or (month==4 and day >=1 and day <=30)  or (month==5 and day>=1 and day<=31)):
    print("Пора года- весна")
# добавил оператор elif который по номеру месяцов 3, 4, 5 и дням определяет весенние месяцы
elif ((month==6 and day >=1 and day <=30) or (month==7 and day >=1 and day <=31)  or (month==8 and day>=1 and day<=31)):
    print("Пора года - лето")
# добавил оператор elif который по номеру месяцов 6, 7, 8 и дням определяет летние месяцы
elif ((month==9 and day >=1 and day <=30) or (month==10 and day >=1 and day <=31)  or (month==11 and day>=1 and day<=30)):
    print("Пора года - осень")
# добавил оператор elif который по номеру месяцов 9, 10, 11 и дням определяет осенние месяцы
else: print("Ошибка ввода ")
# при неправильном введении месяца или дня блок else выдаст ошибку 

