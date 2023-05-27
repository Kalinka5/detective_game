# import modules:
#       playsound to play wav sound.
#       class Hard.
#       class Health_exception.
#       time - to time sleep.
#       json - to read json files.
#       functions choices and all questions.
from playsound import playsound
from hard_mini_games import Hard
from health_exception import Health_exception
import time
import json
from questions import choice1, choice2, question1, question2, question3, question4

# open json file "story" and read it.
with open('story.json', encoding="utf-8") as f:
    story = json.loads(f.read())


# recursive function to read all text-voice story game.
# a variable n – next key in the file json.
def easy(n: str, language: str, audio: str):
    # if key in the json file equals 0, the programme will exit.
    if n == 0:
        input()
        exit()

    # print phrases from story file.
    print(story[n][language]['text'])

    # make time sleep to allow the player to read all the text.
    if audio == 'no' or audio == 'ні':
        time.sleep(story[n]['time'])

    # play each audio recordings.
    elif audio == 'yes' or audio == 'так':
        for voice in story[n][language]['voice'].values():
            if 'ua' in voice:
                playsound(f"audio_ukr/{voice}")
            else:
                playsound(f"audio/{voice}")
        time.sleep(1)       # pause between audio recordings.

    # if type in the json file equals "choice", it will call the function choice().
    if story[n]['interactive']['type'] == 'choice1':
        easy(story[n]['interactive']['next'][choice1(language)], language, audio)
    elif story[n]['interactive']['type'] == 'choice2':
        easy(story[n]['interactive']['next'][choice2(language)], language, audio)

    # call all questions in the end of detective game.
    if story[n]['interactive']['type'] == 'question1':
        question1(language, audio)
    elif story[n]['interactive']['type'] == 'question2':
        question2(language, audio)
    elif story[n]['interactive']['type'] == 'question3':
        question3(language, audio)
    elif story[n]['interactive']['type'] == 'question4':
        question4(language, audio)

    # call itself.
    easy(story[n]['interactive']['next'], language, audio)


# recursive function to read all text-voice hard game.
# a variable n – next key in the file json.
def hard(n: str, language: str, audio: str):
    # if key in the json file equals 0, the programme will exit.
    if n == 0:
        input()
        exit()

    # print phrases from story file.
    print(story[n][language]['text'])

    # make time sleep to allow the player to read all the text.
    if audio == 'no' or audio == 'ні':
        time.sleep(story[n]['time'])

    # play each audio recordings.
    elif audio == 'yes' or audio == 'так':
        for voice in story[n][language]['voice'].values():
            playsound(voice)
        time.sleep(1)  # pause between audio recordings.

    # if level in the story file equals "hard", it will call the functions games.
    if story[n]['interactive']['level'] == 'hard1':
        a.game1(language, audio)
    elif story[n]['interactive']['level'] == 'hard2':
        a.game2(language, audio)
    elif story[n]['interactive']['level'] == 'hard3':
        a.game3(language, audio)

    # if type in the json file equals "choice", it will call the function choice().
    if story[n]['interactive']['type'] == 'choice1':
        hard(story[n]['interactive']['next'][choice1(language)], language, audio)
    elif story[n]['interactive']['type'] == 'choice2':
        hard(story[n]['interactive']['next'][choice2(language)], language, audio)

    # call all questions in the end of detective game.
    elif story[n]['interactive']['type'] == 'question1':
        a.hard_question1(language, audio)
    elif story[n]['interactive']['type'] == 'question2':
        a.hard_question2(language, audio)
    elif story[n]['interactive']['type'] == 'question3':
        a.hard_question3(language, audio)
    elif story[n]['interactive']['type'] == 'question4':
        a.hard_question4(language, audio)

    # call itself.
    hard(story[n]['interactive']['next'], language, audio)


# function to call in the main file.
def game(language: str):
    try:
        # player also can choose play game with audio or without it.
        audio = input(story["1"][language]['text'])
        # if player enters not "yes" or not "no", it will repeat request.
        while audio != 'yes' and audio != 'no' and audio != 'так' and audio != 'ні':
            print(story["2"][language]['text'])
            audio = input(story["1"][language]['text'])
        else:
            # player can choose difficulty level.
            difficult = input(story["3"][language]['text'])
            # if player enters not "story" or not "hard", it will repeat request.
            while difficult != 'story' and difficult != 'hard' and difficult != 'легкий' and difficult != 'важкий':
                print(story["2"][language]['text'])
                difficult = input(story["3"][language]['text'])
            else:
                # call function with story difficulty level.
                if difficult.lower() == 'story' or difficult.lower() == 'легкий':
                    easy("4", language, audio)
                # call function with hard difficulty level.
                elif difficult.lower() == 'hard' or difficult.lower() == 'важкий':
                    hard("5", language, audio)

    # if player didn't enter what he/she asked for.
    except ValueError:
        # You didn't enter what you asked for. GOODBYE...
        print(story["114"][language]['text'])
        if audio == 'no' or audio == 'ні':
            time.sleep(story["114"]['time'])
        elif audio == 'yes' or audio == 'так':
            playsound(story["114"][language]['voice'])
        time.sleep(1)
        # offers to play again.
        if audio == 'yes' or audio == 'так':
            playsound(story["115"][language]['voice'])
        # Do you want to play again? (yes or no)
        restart = input(story["115"][language]['text'])
        match restart:
            case 'yes' | "так":
                game(language)
            case 'no' | "ні":
                # As you wish. Goodbye!
                print(story["116"][language]['text'])
                if audio == 'yes' or audio == 'так':
                    playsound(story["116"][language]['voice'])
    # the exception if player losing all lives.
    except Health_exception:
        # You lost all lives. LOOSER.
        print(story["117"][language]['text'])
        if audio == 'no' or audio == 'ні':
            time.sleep(story["117"]['time'])
        elif audio == 'yes' or audio == 'так':
            playsound(story["117"][language]['voice'])
        time.sleep(1)
        # offers to play again.
        if audio == 'yes' or audio == 'так':
            playsound(story["115"][language]['voice'])
        # Do you want to play again? (yes or no)
        restart = input(story["115"][language]['text'])
        match restart:
            case 'yes' | "так":
                game(language)
            case 'no' | "ні":
                # As you wish. Goodbye!
                print(story["116"][language]['text'])
                if audio == 'yes' or audio == 'так':
                    playsound(story["116"][language]['voice'])


# make object "a" in the Hard class.
a = Hard()
