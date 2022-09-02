def choice():
    num = input('Ви обрали варіант ')
    return num


def question1():
    choice3 = input('Ви думаєте що це був ')
    while choice3.title() != 'Майк' and choice3.title() != 'Майк Вільямс':
        print('Ні, будь ласка, подумайте і дайте відповідь ще раз.')
        choice3 = input('\nХто підпалив торговельний центр? ')


def question2():
    choice4 = input('Ви думаєте що він обпік ')
    while choice4.lower() != 'руки' and choice4.lower() != 'руку':
        print('Ні, будь ласка, подумайте і дайте відповідь ще раз.')
        choice4 = input('\nЯка частина тіла Майка згоріла? ')


def question3():
    choice5 = input('Ви думаєте що це ')
    while choice5 != '7':
        print('Ні, будь ласка, подумайте і дайте відповідь ще раз.')
        choice5 = input('\nЯкого червня сталася пожежа? (число) ')


def question4():
    choice6 = input('Ви думаєте його ')
    while choice6.lower() != 'отруїли':
        print('Ні, будь ласка, подумайте і дайте відповідь ще раз.')
        choice6 = input('\nЯк вбили Майка? (застрелили, зарізали чи отруїли) ')
