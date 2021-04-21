print('Введите число: ', end='')
print(999)
x = 999
first = x // 100

second = x // 10 % 10

third = x % 10

msg = '\u0421\u0443\u043c\u043c\u0430 \u0446\u0438\u0444\u0440 \u0432 \u0447\u0438\u0441\u043b\u0435 \u0440\u0430\u0432\u043d\u0430: '

print(msg, first + second + third)

