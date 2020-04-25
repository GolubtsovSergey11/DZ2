age = int(input('Введите свой возраст: '))
height = int(input('Введите свой рост: '))
amount_of_children = int(input('Сколько у Вас детей: '))
study = input('Вы учитесь сейчас, Да или Нет ').title()

if 18 <= age <= 27:
    if amount_of_children <= 2:
        if study == 'Нет':
            if height <= 170:
                print('В танкисты.')
            elif 170 < height <= 185:
                print('На флот.')
            elif 185 < height <= 200:
                print('В десантники.')
            else:
                print('В другие войска.')
        elif study == 'Да':
            print('Вы учитесь, у Вас отсрочка.')
        else:
            print('Вы не подтвердили учебу.')
    elif amount_of_children > 2:
        print('У Вас больше двух детей, вы не годны.')
elif age < 18:
    print('Вы еще молоды для призыва.')
else:
    print('Вы уже не годны по возрасту.')





