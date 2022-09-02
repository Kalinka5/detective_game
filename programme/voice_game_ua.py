from playsound import playsound
from hard_voice_ua import Hard
from health_exception import Health_exception
import time
import json
from question_voice_ua import choice, question1, question2, question3, question4

with open('story.json', encoding="utf-8") as f:
    story = json.loads(f.read())


def recourse_story(n):
    if n == 0:
        input()
        exit()
    print(story[n]['укр']['text'])
    for voice in story[n]['укр']['voice'].values():
        playsound(voice)
    if story[n]['interactive']['type'] == 'choice':
        recourse_story(story[n]['interactive']['next'][choice()])
    elif story[n]['interactive']['type'] == 'question1':
        question1()
    elif story[n]['interactive']['type'] == 'question2':
        question2()
    elif story[n]['interactive']['type'] == 'question3':
        question3()
    elif story[n]['interactive']['type'] == 'question4':
        question4()
    recourse_story(story[n]['interactive']['next'])


def recourse_hard(n):
    if n == 0:
        input()
        exit()
    print(story[n]["укр"]['text'])
    for voice in story[n]["укр"]['voice'].values():
        playsound(voice)
    if story[n]['interactive']['level'] == 'hard1':
        a.game1()
    elif story[n]['interactive']['level'] == 'hard2':
        a.game2()
    elif story[n]['interactive']['level'] == 'hard3':
        a.game3()
    if story[n]['interactive']['type'] == 'choice':
        recourse_hard(story[n]['interactive']['next'][choice()])
    elif story[n]['interactive']['type'] == 'question1':
        a.choice3()
    elif story[n]['interactive']['type'] == 'question2':
        a.choice4()
    elif story[n]['interactive']['type'] == 'question3':
        a.choice5()
    elif story[n]['interactive']['type'] == 'question4':
        a.choice6()
    recourse_hard(story[n]['interactive']['next'])


def main_voice_ua():
    try:
        difficult = input('\nОберіть рівень складності (легкий або важкий) ')
        while difficult != 'легкий' and difficult != 'важкий':
            print('Ви ввели не те, що просили!')
            difficult = input('\nОберіть рівень складності (легкий або важкий) ')
        else:
            if difficult.lower() == 'легкий':
                recourse_story("1")
            elif difficult.lower() == 'важкий':
                recourse_hard("2")
    except ValueError:
        print('Ви ввели не те, що просили. ДО ПОБАЧЕННЯ...')
        playsound('vrecord_ua106.wav')
        time.sleep(1)
        playsound('vrecord_ua107.wav')
        restart = input('\nХочеш зіграти знову? (так чи ні) ')
        match restart:
            case 'так':
                main_voice_ua()
            case 'ні':
                print('Як побажаєш. До зустрічі!')
                playsound('vrecord_ua108.wav')
    except Health_exception:
        print('\nВи втратили всі життя.\nЛУЗЕР.')
        playsound('vrecord_ua109.wav')
        time.sleep(1)
        playsound('vrecord_ua107.wav')
        restart = input('\nХочеш зіграти знову? (так чи ні) ')
        match restart:
            case 'так':
                main_voice_ua()
            case 'ні':
                print('Як побажаєш. До зустрічі!')
                playsound('vrecord_ua108.wav')


a = Hard()
