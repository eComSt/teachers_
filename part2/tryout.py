try:
    a = int(input("1:"))
    b = int(input("2:"))
    result = a%b
except ZeroDivisionError:
    b = int(input("На ноль делить нельзя! Введите другое число:"))
except ValueError:
    a = int(input("Нужно ввести целое число! Введите другое число:"))
    b = int(input("Нужно ввести целое число! Введите другое число:"))
except:
    print('Неизвестная ошибка!')
else:
    print(f"Остаток от деления {a} на {b} равно {result}")
finally:
    result = a%b
    print(f"Остаток от деления {a} на {b} равно {result}")

