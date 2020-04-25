date = int(input('Введите число: '))
month = input('Введите месяц: ').title()

if (month == 'Март' and date >= 21) or (month == 'Апрель' and date <= 20):
    print('Овен')
elif (month == 'Апрель' and date >= 21) or (month == 'Май' and date <= 21):
    print('Телец')
elif (month == 'Май' and date >= 22) or (month == 'Июнь' and date <= 21):
    print('Близнецы')
elif (month == 'Июнь' and date >= 22) or (month == 'Июль' and date <= 22):
    print('Рак')
elif (month == 'Июль' and date >= 23) or (month == 'Август' and date <= 21):
    print('Лев')
elif (month == 'Август' and date >= 22) or (month == 'Сентябрь' and date <= 23):
    print('Дева')
elif (month == 'Сентябрь' and date >= 24) or (month == 'Октябрь' and date <= 23):
    print('Весы')
elif (month == 'Октябрь' and date >= 24) or (month == 'Ноябрь' and date <= 22):
    print('Скорпион')
elif (month == 'Ноябрь' and date >= 23) or (month == 'Декабрь' and date <= 22):
    print('Стрелец')
elif (month == 'Декабрь' and date >= 23) or (month == 'Январь' and date <= 20):
    print('Кознрог')
elif (month == 'Январь' and date >= 21) or (month == 'Февраль' and date <= 19):
    print('Водолей')
elif (month == 'Февраль' and date >= 20) or (month == 'Март' and date <= 20):
    print('Рыбы')
else:
    print('Некоректный ввод')
