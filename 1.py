# Условие задач
# 1. Найти сумму и произведение цифр введённого 3х-значного натурального числа.
# Например, если введено число 325,
# то сумма его цифр равна 10 (3+2+5), а произведение - 30 (325).
try:
    a1 = int(input("ВВедите 3-х значное число: "))
    if 99 < a1 < 1000:
        a2 = int(str(a1)[0]) + int(str(a1)[1]) + int(str(a1)[2])
        a3 = int(str(a1)[0]) * int(str(a1)[1]) * int(str(a1)[2])
        print('введено число ', a1, '\nCумма его цифр равна ', a2, ',\nа его произведение равно ', a3)
    else:
        print("число не 3-х значное")
except ValueError:
        print("вы ввели не число а строку")