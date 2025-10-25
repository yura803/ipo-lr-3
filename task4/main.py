# Задал правильный пароль
correct_password = "bobrinoe kopito"

# Просим пользователя ввести пароль 
user_password = input("Введите пароль: ")

# Проверяем правильный ли пароль
if user_password == correct_password:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")
    print("Неправильный пароль")
