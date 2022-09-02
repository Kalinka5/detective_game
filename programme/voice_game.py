from playsound import playsound
from hard_voice import Hard
from health_exception import Health_exception
import time
import json
from question_voice import choice, question1, question2, question3, question4

with open('story.json', encoding="utf-8") as f:
    story = json.loads(f.read())


def recourse_story(n):
    if n == 0:
        input()
        exit()
    print(story[n]['en']['text'])
    for voice in story[n]['en']['voice'].values():
        playsound(voice)
    time.sleep(1)
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
    print(story[n]['en']['text'])
    for voice in story[n]['en']['voice'].values():
        playsound(voice)
    time.sleep(1)
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


def main_voice():
    try:
        difficult = input('\nSelect difficulty level (story or hard) ')
        while difficult != 'story' and difficult != 'hard':
            print('You didn\'t enter what you asked for!')
            difficult = input('\nSelect difficulty level (story or hard) ')
        else:
            if difficult.lower() == 'story':
                recourse_story("1")
            elif difficult.lower() == 'hard':
                recourse_hard("2")
    except ValueError:
        print('You didn\'t enter what you asked for. GOODBYE...')
        playsound('vvauthor_say64.wav')
        time.sleep(1)
        playsound('vvauthor_say65.wav')
        restart = input('\nDo you want to play again? (yes or no) ')
        match restart:
            case 'yes':
                main_voice()
            case 'no':
                print('As you wish. Goodbye!')
                playsound('vvauthor_say66.wav')
    except Health_exception:
        print('\nYou lost all lives\nLOOSER.')
        playsound('vvauthor_say67.wav')
        time.sleep(1)
        playsound('vvauthor_say65.wav')
        restart = input('\nDo you want to play again? (yes or no) ')
        match restart:
            case 'yes':
                main_voice()
            case 'no':
                print('As you wish. Goodbye!')
                playsound('vvauthor_say66.wav')


a = Hard()
