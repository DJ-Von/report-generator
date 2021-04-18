x = int(input("Введите число: "))
first = x//100
second = x//10%10
third = x%10
msg = "Сумма цифр в числе равна: "
print(msg, first+second+third)
