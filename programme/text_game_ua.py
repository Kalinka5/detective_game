# імпортує модулі:
#       клас Hard.
#       клас Health_exception.
#       time - для сну комп'ютера.
#       json - щоб читати json файли.
#       функції choice і всі питання.
from hard_text_ua import Hard_ua
from health_exception import Health_exception
import time
import json
from question_text_ua import choice, question1, question2, question3, question4

# відкриває json файл "story" та читає його.
with open('story.json', encoding="utf-8") as f:
    story = json.loads(f.read())


# рекурсивна функція щоб прочитати усю текстову легку гру.
# змінна n – це наступний ключ у файлі json.
def text_story(n):
    # якщо ключ у json файлі дорівнює 0, то програма закінчиться.
    if n == 0:
        input()
        exit()

    print(story[n]['укр']['text'])      # надрукує текст з файла json.
    time.sleep(story[n]['time'])        # викликає функцію sleep, щоб гравець встиг прочитати весь текст.

    # якщо тип у json файлі дорівнює "choice", то викликається функція choice().
    if story[n]['interactive']['type'] == 'choice':
        text_story(story[n]['interactive']['next'][choice()])

    # викликаються усі питання у кінці детективної гри.
    elif story[n]['interactive']['type'] == 'question1':
        question1()
    elif story[n]['interactive']['type'] == 'question2':
        question2()
    elif story[n]['interactive']['type'] == 'question3':
        question3()
    elif story[n]['interactive']['type'] == 'question4':
        question4()

    # викликає сама себе у при кінці.
    text_story(story[n]['interactive']['next'])


# рекурсивна функція, щоб прочитати усю текстову важку гру.
# змінна n – це наступний ключ у файлі json.
def text_hard(n):
    # якщо ключ у json файлі дорівнює 0, то програма закінчиться.
    if n == 0:
        input()
        exit()

    print(story[n]['укр']['text'])      # надрукує текст з файла json.
    time.sleep(story[n]['time'])        # викликає функцію sleep, щоб гравець встиг прочитати весь текст.

    # якщо level у json файлі дорівнюють "hard(1, 2, 3)", то викликаються функції game1(), 2(), 3()
    if story[n]['interactive']['level'] == 'hard1':
        a.game1()
    elif story[n]['interactive']['level'] == 'hard2':
        a.game2()
    elif story[n]['interactive']['level'] == 'hard3':
        a.game3()

    # якщо тип у json файлі дорівнює "choice", то викликається функція choice().
    if story[n]['interactive']['type'] == 'choice':
        text_hard(story[n]['interactive']['next'][choice()])

    # викликаються усі питання у кінці детективної гри.
    elif story[n]['interactive']['type'] == 'question1':
        a.choice3()
    elif story[n]['interactive']['type'] == 'question2':
        a.choice4()
    elif story[n]['interactive']['type'] == 'question3':
        a.choice5()
    elif story[n]['interactive']['type'] == 'question4':
        a.choice6()

    # викликає сама себе у при кінці.
    text_hard(story[n]['interactive']['next'])


# функція викликається у main файлі.
def main_text_ua():
    try:
        # гравець може обрати рівень складності.
        difficult = input('\nОберіть рівень складності (легкий або важкий) ')
        # якщо гравець вводить не «легкий» або не «важкий», то програма повторюватиме запит.
        while difficult != 'легкий' and difficult != 'важкий':
            print('Ви ввели не те, що просили!')
            difficult = input('\nОберіть рівень складності (легкий або важкий) ')
        else:
            if difficult.lower() == 'легкий':
                text_story("1")     # викликається функція гри легкого рівня складності.
            elif difficult.lower() == 'важкий':
                text_hard("2")      # викликається функція гри важкого рівня складності.

    # якщо гравець ввів не те що потрібно.
    except ValueError:
        print('Ви ввели не те, що просили. ДО ПОБАЧЕННЯ...')
        time.sleep(3)
        # пропонує зіграти знову.
        restart = input('Хочеш зіграти знову? (так чи ні) ')
        match restart:
            case 'так':
                main_text_ua()
            case 'ні':
                print('Як побажаєш. До зустрічі!')
    # виняток, якщо гравець витратив усі життя.
    except Health_exception:
        print('\nВи втратили всі життя.\nЛУЗЕР.')
        time.sleep(2)
        # пропонує зіграти знову.
        restart = input('\nХочеш зіграти знову? (так чи ні) ')
        match restart:
            case 'так':
                main_text_ua()
            case 'ні':
                print('Як побажаєш. До зустрічі!')


# об'єкт "a" у Hard класі.
a = Hard_ua()
