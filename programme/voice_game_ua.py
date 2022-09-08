# імпортує модулі:
#       playsound - для відкриття аудіо файлів.
#       клас Hard.
#       клас Health_exception.
#       time - для сну комп'ютера.
#       json - щоб читати json файли.
#       функції choice і всі питання.
from playsound import playsound
from hard_voice_ua import Hard
from health_exception import Health_exception
import time
import json
from question_voice_ua import choice, question1, question2, question3, question4

# відкриває json файл "story" та читає його.
with open('story.json', encoding="utf-8") as f:
    story = json.loads(f.read())


# рекурсивна функція щоб прочитати усю текстову легку гру.
# змінна n – це наступний ключ у файлі json.
def recourse_story(n):
    # якщо ключ у json файлі дорівнює 0, то програма закінчиться.
    if n == 0:
        input()
        exit()

    print(story[n]['укр']['text'])      # надрукує текст з файла json.

    # відтворює всі аудіозаписи.
    for voice in story[n]['укр']['voice'].values():
        playsound(voice)

    # якщо тип у json файлі дорівнює "choice", то викликається функція choice().
    if story[n]['interactive']['type'] == 'choice':
        recourse_story(story[n]['interactive']['next'][choice()])

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
    recourse_story(story[n]['interactive']['next'])


# рекурсивна функція, щоб прочитати усю аудіотекстову важку гру.
# змінна n – це наступний ключ у файлі json.
def recourse_hard(n):
    # якщо ключ у json файлі дорівнює 0, то програма закінчиться.
    if n == 0:
        input()
        exit()

    print(story[n]["укр"]['text'])      # надрукує текст з файла json.

    # відтворює всі аудіозаписи.
    for voice in story[n]["укр"]['voice'].values():
        playsound(voice)

    # якщо level у json файлі дорівнюють "hard(1, 2, 3)", то викликаються функції game1(), 2(), 3()
    if story[n]['interactive']['level'] == 'hard1':
        a.game1()
    elif story[n]['interactive']['level'] == 'hard2':
        a.game2()
    elif story[n]['interactive']['level'] == 'hard3':
        a.game3()

    # якщо тип у json файлі дорівнює "choice", то викликається функція choice().
    if story[n]['interactive']['type'] == 'choice':
        recourse_hard(story[n]['interactive']['next'][choice()])

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
    recourse_hard(story[n]['interactive']['next'])


# функція викликається у main файлі.
def main_voice_ua():
    try:
        # гравець може обрати рівень складності.
        difficult = input('\nОберіть рівень складності (легкий або важкий) ')
        # якщо гравець вводить не «легкий» або не «важкий», то програма повторюватиме запит.
        while difficult != 'легкий' and difficult != 'важкий':
            print('Ви ввели не те, що просили!')
            difficult = input('\nОберіть рівень складності (легкий або важкий) ')
        else:
            if difficult.lower() == 'легкий':
                recourse_story("1")     # викликається функція гри легкого рівня складності.
            elif difficult.lower() == 'важкий':
                recourse_hard("2")      # викликається функція гри важкого рівня складності.

    # якщо гравець ввів не те що потрібно.
    except ValueError:
        print('Ви ввели не те, що просили. ДО ПОБАЧЕННЯ...')
        playsound('vrecord_ua106.wav')
        time.sleep(1)
        playsound('vrecord_ua107.wav')
        # пропонує зіграти знову.
        restart = input('\nХочеш зіграти знову? (так чи ні) ')
        match restart:
            case 'так':
                main_voice_ua()
            case 'ні':
                print('Як побажаєш. До зустрічі!')
                playsound('vrecord_ua108.wav')
    # виняток, якщо гравець витратив усі життя.
    except Health_exception:
        print('\nВи втратили всі життя.\nЛУЗЕР.')
        playsound('vrecord_ua109.wav')
        time.sleep(1)
        playsound('vrecord_ua107.wav')
        # пропонує зіграти знову.
        restart = input('\nХочеш зіграти знову? (так чи ні) ')
        match restart:
            case 'так':
                main_voice_ua()
            case 'ні':
                print('Як побажаєш. До зустрічі!')
                playsound('vrecord_ua108.wav')


# об'єкт "a" у Hard класі.
a = Hard()
