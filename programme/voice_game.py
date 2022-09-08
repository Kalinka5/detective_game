# import modules:
#       playsound to play wav sound.
#       class Hard.
#       class Health_exception.
#       time - to time sleep.
#       json - to read json files.
#       function choice and all questions.
from playsound import playsound
from hard_voice import Hard
from health_exception import Health_exception
import time
import json
from question_voice import choice, question1, question2, question3, question4

# open json file "story" and read it.
with open('story.json', encoding="utf-8") as f:
    story = json.loads(f.read())


# recursive function to read all text-voice story game.
# a variable n – next key in the file json.
def voice_story(n):
    # if key in the json file equals 0, the programme will exit.
    if n == 0:
        input()
        exit()

    print(story[n]['en']['text'])       # print text from json file.

    # play each audio recordings.
    for voice in story[n]['en']['voice'].values():
        playsound(voice)
    time.sleep(1)       # pause between audio recordings.

    # if type in the json file equals "choice", it will call the function choice().
    if story[n]['interactive']['type'] == 'choice':
        voice_story(story[n]['interactive']['next'][choice()])

    # call all questions in the end of detective game.
    elif story[n]['interactive']['type'] == 'question1':
        question1()
    elif story[n]['interactive']['type'] == 'question2':
        question2()
    elif story[n]['interactive']['type'] == 'question3':
        question3()
    elif story[n]['interactive']['type'] == 'question4':
        question4()

    # call itself.
    voice_story(story[n]['interactive']['next'])


# recursive function to read all text-voice hard game.
# a variable n – next key in the file json.
def voice_hard(n):
    # if key in the json file equals 0, the programme will exit.
    if n == 0:
        input()
        exit()

    print(story[n]['en']['text'])       # print text from json file.

    # play each audio recordings.
    for voice in story[n]['en']['voice'].values():
        playsound(voice)
    time.sleep(1)       # pause between audio recordings.

    # if level in the json file equals "hard(1, 2, 3)", it will call the functions game1(), 2(), 3()
    if story[n]['interactive']['level'] == 'hard1':
        a.game1()
    elif story[n]['interactive']['level'] == 'hard2':
        a.game2()
    elif story[n]['interactive']['level'] == 'hard3':
        a.game3()

    # if type in the json file equals "choice", it will call the function choice().
    if story[n]['interactive']['type'] == 'choice':
        voice_hard(story[n]['interactive']['next'][choice()])

    # call all questions in the end of detective game.
    elif story[n]['interactive']['type'] == 'question1':
        a.choice3()
    elif story[n]['interactive']['type'] == 'question2':
        a.choice4()
    elif story[n]['interactive']['type'] == 'question3':
        a.choice5()
    elif story[n]['interactive']['type'] == 'question4':
        a.choice6()

    # call itself.
    voice_hard(story[n]['interactive']['next'])


# function to call in the main file.
def main_voice():
    try:
        # player can choose difficulty level.
        difficult = input('\nSelect difficulty level (story or hard) ')
        # if player enters not "story" or not "hard", it will repeat request.
        while difficult != 'story' and difficult != 'hard':
            print('You didn\'t enter what you asked for!')
            difficult = input('\nSelect difficulty level (story or hard) ')
        else:
            if difficult.lower() == 'story':
                voice_story("1")        # call function with story difficulty level.
            elif difficult.lower() == 'hard':
                voice_hard("2")         # call function with hard difficulty level.

    # if player didn't enter what he/she asked for.
    except ValueError:
        print('You didn\'t enter what you asked for. GOODBYE...')
        playsound('vvauthor_say64.wav')
        time.sleep(1)
        playsound('vvauthor_say65.wav')
        # offers to play again.
        restart = input('\nDo you want to play again? (yes or no) ')
        match restart:
            case 'yes':
                main_voice()
            case 'no':
                print('As you wish. Goodbye!')
                playsound('vvauthor_say66.wav')
    # the exception if player losing all lives.
    except Health_exception:
        print('\nYou lost all lives\nLOOSER.')
        playsound('vvauthor_say67.wav')
        time.sleep(1)
        playsound('vvauthor_say65.wav')
        # offers to play again.
        restart = input('\nDo you want to play again? (yes or no) ')
        match restart:
            case 'yes':
                main_voice()
            case 'no':
                print('As you wish. Goodbye!')
                playsound('vvauthor_say66.wav')


# make object "a" in the Hard class.
a = Hard()
