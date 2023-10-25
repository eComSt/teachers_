name = input("Введите имя")
file = open(f"log_calc.txt", "a",encoding="utf-8")
file.write(f'{name}\n')
while True:
    try:
        a = int(input("Первое число:"))
        oper = input("Операция: + - * / ** // %:")
        b = int(input("Второе число:"))
        file.write(f"{a} {oper} {b}\n")
        result = eval(f"{a}{oper}{b}")
    except ZeroDivisionError:
        b = int(input("На ноль делить нельзя! Введите другое число:"))
        file.write("На ноль делить нельзя\n")
        file.write(f"{b}\n")
    except ValueError:
        a = int(input("Нужно ввести целое число! Введите другое число:"))
        b = int(input("Нужно ввести целое число! Введите другое число:"))
        file.write("некорректный ввод\n")
        file.write(f"{a}\n")
        file.write(f"{b}\n")
    except SyntaxError:
        print('Ситаксическая ошибка!')
        oper = input("Операция: + - * / ** // %:")
        file.write("некорректный ввод операции\n")
        file.write(f"{oper}\n")
    else:
        print(f" отделения {a} на {b} равно {result}")
    finally:
        result = eval(f"{a}{oper}{b}")
        file.write(f"{a} {oper} {b} равно {result}")
        is_continue = input("Продолжать? y/n:")
        if is_continue == "n":
            print('Good bye!')
            file.write("______________")
            file.close()
            break
        file.close()