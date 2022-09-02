from hard_text_ua import Hard_ua
from health_exception import Health_exception
import time
import json
from question_text_ua import choice, question1, question2, question3, question4

with open('story.json', encoding="utf-8") as f:
    story = json.loads(f.read())


def text_story(n):
    if n == 0:
        input()
        exit()
    print(story[n]['укр']['text'])
    time.sleep(story[n]['time'])
    if story[n]['interactive']['type'] == 'choice':
        text_story(story[n]['interactive']['next'][choice()])
    elif story[n]['interactive']['type'] == 'question1':
        question1()
    elif story[n]['interactive']['type'] == 'question2':
        question2()
    elif story[n]['interactive']['type'] == 'question3':
        question3()
    elif story[n]['interactive']['type'] == 'question4':
        question4()
    text_story(story[n]['interactive']['next'])


def text_hard(n):
    if n == 0:
        input()
        exit()
    print(story[n]['укр']['text'])
    time.sleep(story[n]['time'])
    if story[n]['interactive']['level'] == 'hard1':
        a.game1()
    elif story[n]['interactive']['level'] == 'hard2':
        a.game2()
    elif story[n]['interactive']['level'] == 'hard3':
        a.game3()
    if story[n]['interactive']['type'] == 'choice':
        text_hard(story[n]['interactive']['next'][choice()])
    elif story[n]['interactive']['type'] == 'question1':
        a.choice3()
    elif story[n]['interactive']['type'] == 'question2':
        a.choice4()
    elif story[n]['interactive']['type'] == 'question3':
        a.choice5()
    elif story[n]['interactive']['type'] == 'question4':
        a.choice6()
    text_hard(story[n]['interactive']['next'])


def main_text_ua():
    try:
        difficult = input('\nОберіть рівень складності (легкий або важкий) ')
        while difficult != 'легкий' and difficult != 'важкий':
            print('Ви ввели не те, що просили!')
            difficult = input('\nОберіть рівень складності (легкий або важкий) ')
        else:
            if difficult.lower() == 'легкий':
                text_story("1")
            elif difficult.lower() == 'важкий':
                text_hard("2")

    except ValueError:
        print('Ви ввели не те, що просили. ДО ПОБАЧЕННЯ...')
        time.sleep(2)
        restart = input('Хочеш зіграти знову? (так чи ні) ')
        match restart:
            case 'так':
                main_text_ua()
            case 'ні':
                print('Як побажаєш. До зустрічі!')
    except Health_exception:
        print('\nВи втратили всі життя.\nЛУЗЕР.')
        time.sleep(2)
        restart = input('\nХочеш зіграти знову? (так чи ні) ')
        match restart:
            case 'так':
                main_text_ua()
            case 'ні':
                print('Як побажаєш. До зустрічі!')


a = Hard_ua()
