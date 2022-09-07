# if type equals "choice" it will call this function.
# this function returns only choice number.
def choice():
    num = input('You chose the option number ')
    return num


# function to ask the question1.
def question1():
    choice3 = input('You think it was ')
    # if answer not equals "Mike" or "Mike Williams" it will repeat the question.
    # use function title to make big first letter.
    while choice3.title() != 'Mike' and choice3.title() != 'Mike Williams':
        print('No, please think and answer again.')
        choice3 = input('\nWho set fire to the mall? ')


# function to ask the question2.
def question2():
    choice4 = input('You think he burned ')
    # if answer not equals "hands", "hand" or "arms" it will repeat the question.
    # use the function lower to make word with small letters.
    while choice4.lower() != 'hands' and choice4.lower() != 'hand' and choice4.lower() != 'arms':
        print('No, please think and answer again.')
        choice4 = input('\nWhat body part did Mike burn? ')


# function to ask the question3.
def question3():
    choice5 = input('You think it was June ')
    # if answer not equals "7" or "7th" it will repeat the question.
    # use the function lower to make word with small letters.
    while choice5 != '7' and choice5 != '7th':
        print('No, please think and answer again.')
        choice5 = input('\nWhat June did the fire happen? (number) ')


# function to ask the question4.
def question4():
    choice6 = input('You think he was ')
    # if answer not equals "poisoned" it will repeat the question.
    # use the function lower to make word with small letters.
    while choice6.lower() != 'poisoned':
        print('No, please think and answer again.')
        choice6 = input('\nHow was Mike killed? (shot, stabbed or poisoned) ')
