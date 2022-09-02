def choice():
    num = input('You chose the option number ')
    return num


def question1():
    choice3 = input('You think it was ')
    while choice3.title() != 'Mike' and choice3.title() != 'Mike Williams':
        print('No, please think and answer again.')
        choice3 = input('\nWho set fire to the mall? ')


def question2():
    choice4 = input('You think he burned ')
    while choice4.lower() != 'hands' and choice4.lower() != 'hand' and choice4.lower() != 'arms':
        print('No, please think and answer again.')
        choice4 = input('\nWhat body part did Mike burn? ')


def question3():
    choice5 = input('You think it was June ')
    while choice5 != '7' and choice5 != '7th':
        print('No, please think and answer again.')
        choice5 = input('\nWhat June did the fire happen? (number) ')


def question4():
    choice6 = input('You think he was ')
    while choice6.lower() != 'poisoned':
        print('No, please think and answer again.')
        choice6 = input('\nHow was Mike killed? (shot, stabbed or poisoned) ')