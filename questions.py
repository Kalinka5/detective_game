# import modules:
#       playsound to open audio files.
#       json to read json files.
from playsound import playsound
import json

# open json file "story" and read it.
with open('story.json', encoding="utf-8") as f:
    story = json.loads(f.read())


# if type equals "choice" it will call this function.
# this function returns only choice number.
def choice1(language: str) -> str:
    # You chose the option number...
    num = input(story["104"][language]['text'])
    match num:
        # if player enter "1", "2" or "3" it will return this numbers of ways.
        case "1" | "2" | "3":
            return num
        # else computer will automatically choose number "3".
        case _:
            return "3"


def choice2(language: str) -> str:
    # You chose the option number...
    num = input(story["104"][language]['text'])
    match num:
        # if player enter "1" or "2" it will return this numbers of ways.
        case "1" | "2":
            return num
        # else computer will automatically choose number "2".
        case _:
            return "2"


# function to ask the question1.
def question1(language: str, audio: str):
    # Who set fire to the mall?
    print(story["80"][language]['text'])
    if audio == 'yes' or audio == 'так':
        playsound(story["80"][language]['voice'])
    # You think it was...
    choice3 = input(story["81"][language]['text'])
    # if answer not equals "Mike" or "Mike Williams" it will repeat the question.
    # use function title to make big first letter.
    match choice3.title():
        case 'Mike' | 'Mike Williams' | 'Майк' | 'Майк Вільямс':
            return "Win"
        case _:
            # No, please think and answer again.
            print(story["105"][language]['text'])
            if audio == 'yes' or audio == 'так':
                playsound(story["105"][language]['voice'])
            # call function question1 again.
            question1(language, audio)


# function to ask the question2.
def question2(language: str, audio: str):
    # What body part did Mike burn?
    print(story["84"][language]['text'])
    if audio == 'yes' or audio == 'так':
        playsound(story["84"][language]['voice'])
    # You think he burned...
    choice4 = input(story["85"][language]['text'])
    # if answer not equals "hands", "hand" or "arms" it will repeat the question.
    # use the function lower to make word with small letters.
    match choice4.lower():
        case 'hands' | 'hand' | 'arms' | 'руки' | 'руку':
            return "Win"
        case _:
            # No, please think and answer again.
            print(story["105"][language]['text'])
            if audio == 'yes' or audio == 'так':
                playsound(story["105"][language]['voice'])
            # call function question2 again.
            question2(language, audio)


# function to ask the question3.
def question3(language: str, audio: str):
    # What June did the fire happen? (number)
    print(story["88"][language]['text'])
    if audio == 'yes' or audio == 'так':
        playsound(story["88"][language]['voice'])
    # You think it was June...
    choice5 = input(story["89"][language]['text'])
    # if answer not equals "7" or "7th" it will repeat the question.
    # use the function lower to make word with small letters.
    match choice5.lower():
        case '7' | '7th':
            return "Win"
        case _:
            # No, please think and answer again.
            print(story["105"][language]['text'])
            if audio == 'yes' or audio == 'так':
                playsound(story["105"][language]['voice'])
            # call function question3 again.
            question3(language, audio)


# function to ask the question4.
def question4(language: str, audio: str):
    # How was Mike killed? (shot, stabbed or poisoned)
    print(story["91"][language]['text'])
    if audio == 'yes' or audio == 'так':
        playsound(story["91"][language]['voice'])
    # You think he was...
    choice6 = input(story["92"][language]['text'])
    # if answer not equals "poisoned" it will repeat the question.
    # use the function lower to make word with small letters.
    match choice6.lower():
        case 'poisoned' | 'отруїли':
            return "Win"
        case _:
            # No, please think and answer again.
            print(story["105"][language]['text'])
            if audio == 'yes' or audio == 'так':
                playsound(story["105"][language]['voice'])
            # call function question3 again.
            question4(language, audio)
