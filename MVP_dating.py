boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

couple = list(zip(boys, girls))
if len(boys) == len(girls):
    print('Идеальные пары:')
    for perfect_couple in couple:
        print(f'{perfect_couple[0]} и {perfect_couple[1]}')
else:
    if len(boys) > len(girls):
        print(boys[-1], 'останется без пары')
    else:
        print(girls[-1], 'останется без пары')
