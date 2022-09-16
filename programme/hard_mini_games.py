# import modules:
#       random to make random numbers,
#       time to time sleep,
#       json to read json files,
#       Health_exception to game over if player loose all lives,
#       playsound to play wav sound.
import random
import time
import json
from health_exception import Health_exception
from playsound import playsound

# open json file "story" and read it.
with open('story.json', encoding="utf-8") as f:
    story = json.loads(f.read())


# class Hard to track the numbers of lives.
class Hard:

    def __init__(self):
        self._health = 10       # create 10 lives to character.
        self.DICE_ART = {       # create more elegant image to short game "Dice rolling".
            1: (
                "┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘",
            ),
            2: (
                "┌─────────┐",
                "│  ●      │",
                "│         │",
                "│      ●  │",
                "└─────────┘",
            ),
            3: (
                "┌─────────┐",
                "│  ●      │",
                "│    ●    │",
                "│      ●  │",
                "└─────────┘",
            ),
            4: (
                "┌─────────┐",
                "│  ●   ●  │",
                "│         │",
                "│  ●   ●  │",
                "└─────────┘",
            ),
            5: (
                "┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘",
            ),
            6: (
                "┌─────────┐",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "└─────────┘",
            ),
        }
        self.DICE_HEIGHT = len(self.DICE_ART[1])
        self.DICE_WIDTH = len(self.DICE_ART[1][0])
        self.DICE_FACE_SEPARATOR = " "

    # First game "Guess the number".
    # a variable language save the selected player's language (english or ukrainian).
    # a variable audio save the selected player's choice (play game with sound or without).
    def game1(self, language: str, audio: str):
        # This game named "Guess the number". The computer guessed a number from 1 to 10...
        print(story["106"][language]['text'])
        # make time sleep to allow the player to read all the text.
        if audio == 'no' or audio == 'ні':
            time.sleep(story["106"]['time'])
        # play audio recording.
        elif audio == 'yes' or audio == 'так':
            playsound(story["106"][language]['voice'])
            time.sleep(1)  # pause between audio recordings.

        clue = 1            # make amount of the clues to give it in the game.
        number = 7          # computer guessed number 7 cause the shopping mall was burned on June 7th.

        # play audio recording.
        if audio == 'yes' or audio == 'так':
            playsound(story["107"][language]['voice'])
        # Choose number (from 1 to 10):
        num = int(input(story["107"][language]['text']))

        all_num = set()     # make set, which don't show the repeated numbers.

        while num != number:        # make the while loop to check is player's num equals computer's number.
            self._health -= 1       # if player doesn't guess the number 1 life will take away.
            if self._health == 0:   # if lives ends it will raise the exception.
                raise Health_exception(self._health)

            all_num.add(num)        # add chosen num.

            # print some loose phrases in english or ukrainian.
            if language == "en":
                print(f'\nOhh... You`re loose!\nMinus 1 point.\nYou have left {self._health} lives.')
                if audio == 'no':
                    time.sleep(7)
                elif audio == 'yes':
                    playsound('vvauthor_say56.wav')
            elif language == "укр":
                print(f'\nОй... Не вгадав!\nВи втратили одне життя.\nУ вас залишилося життів {self._health}.')
                if audio == 'ні':
                    time.sleep(7)
                elif audio == 'так':
                    playsound('vrecord_ua112.wav')

            # give first clue.
            if clue == 1:
                # I'll give you a clue. This number is greater than 5.
                print(story["108"][language]['text'])
                # make time sleep to allow the player to read all the text.
                if audio == 'no' or audio == 'ні':
                    time.sleep(story["108"]['time'])
                # play audio recording.
                elif audio == 'yes' or audio == 'так':
                    playsound(story["108"][language]['voice'])

            # give second clue.
            elif clue == 2:
                # I'll give you one more clue. This is odd number.
                print(story["109"][language]['text'])
                # make time sleep to allow the player to read all the text.
                if audio == 'no' or audio == 'ні':
                    time.sleep(story["109"]['time'])
                # play each audio recordings.
                elif audio == 'yes' or audio == 'так':
                    playsound(story["109"][language]['voice'])

            # print all chosen player's numbers in english or ukrainian.
            if language == "en":
                print(f'\n(You have chosen {sorted(all_num)})')
            elif language == "укр":
                print(f'\n(Ти вже обрав {sorted(all_num)})')

            # player again choose the number.
            if audio == 'yes' or audio == 'так':
                playsound(story["107"][language]['voice'])
            num = int(input(story["107"][language]['text']))
            clue += 1       # to show one clue in one circle and another clue in the other.

        else:               # if player's num equals computer's number, you win.
            if language == "en":
                print(f'\nCongratulations, you win!!!\nYou have left {self._health} lives.')
                if audio == 'no':
                    time.sleep(6)
                elif audio == 'yes':
                    playsound('vvauthor_say59.wav')

            elif language == "укр":
                print(f'\nМої вітання, ви перемогли!!!\nУ вас залишилося життів {self._health}.')
                if audio == 'ні':
                    time.sleep(6)
                elif audio == 'так':
                    playsound('vrecord_ua115.wav')
            time.sleep(1)
            return 1

    # Second game "Dice rolling".
    def game2(self, language: str, audio: str):
        # This game named "Dice rolling".
        # You must roll the dice and the sum of the digits must be greater than or equal to 8.
        print(story["110"][language]['text'])
        # make time sleep to allow the player to read all the text.
        if audio == 'no' or audio == 'ні':
            time.sleep(story["110"]['time'])
        # play audio recording.
        elif audio == 'yes' or audio == 'так':
            for voice in story["110"][language]['voice'].values():
                playsound(voice)
        time.sleep(1)

        # play audio recording.
        if audio == 'yes' or audio == 'так':
            playsound(story["111"][language]['voice'])
        # Please write word "throw" .
        input(story["111"][language]['text'])

        # generate a list of random choices.
        rand_choice = []
        # add to the list random choices with module random.
        for i in range(2):
            rand_choice.append(random.randint(1, 6))

        while True:
            # generate a list of dice faces from DICE_ART
            dice_faces = []
            for value in rand_choice:
                dice_faces.append(self.DICE_ART[value])

            # generate a list containing the dice faces rows
            dice_faces_rows = []
            for row_idx in range(self.DICE_HEIGHT):
                row_components = []
                for die in dice_faces:
                    row_components.append(die[row_idx])
                row_string = self.DICE_FACE_SEPARATOR.join(row_components)
                dice_faces_rows.append(row_string)

            # generate header with the word "RESULTS" centered
            width = len(dice_faces_rows[0])
            diagram_header = " RESULTS ".center(width, "~")

            # diagram_header join with dice_faces_rows
            dice_face_diagram = "\n".join([diagram_header] + dice_faces_rows)
            print(f"\n{dice_face_diagram}")

            # check if sum of the digits greater than or equal to 8.
            # english or ukrainian.
            if (rand_choice[0] + rand_choice[1]) >= 8:
                if language == "en":
                    print(f"You win. Lives have left {self._health}.")
                    if audio == 'no':
                        time.sleep(4)
                    elif audio == 'yes':
                        playsound('vvauthor_say62.wav')
                elif language == "укр":
                    print(f"Ви перемогли. Життів залишилося {self._health}.")
                    if audio == 'ні':
                        time.sleep(4)
                    elif audio == 'так':
                        playsound('vrecord_ua119.wav')
                time.sleep(1)
                break

            self._health -= 1       # else 1 life will take away.
            # print some loose phrases in english or ukrainian.
            if language == "en":
                print(f'Bad luck. Lives have left {self._health}.')
                if audio == 'no':
                    time.sleep(4)
                elif audio == 'yes':
                    playsound('vvauthor_say63.wav')
            elif language == "укр":
                print(f'Погана вдача. Життів залишилося {self._health}.')
                if audio == 'ні':
                    time.sleep(4)
                elif audio == 'так':
                    playsound('vrecord_ua120.wav')

            if self._health == 0:   # if lives ends it will raise the exception.
                raise Health_exception(self._health)

            # player again throw the dice.
            if audio == 'yes' or audio == 'так':
                playsound(story["111"][language]['voice'])
            input(story["111"][language]['text'])
            rand_choice = []
            for i in range(2):
                rand_choice.append(random.randint(1, 6))
        return 1

    # Third game "Rock, paper, scissors".
    def game3(self, language: str, audio: str):
        # make tuple with 3 choices "rock", "paper" or "scissors" and ukrainian version.
        game_list = tuple()
        if language == "en":
            game_list = ('rock', 'paper', 'scissors')
        elif language == "укр":
            game_list = ('камінь', 'папір', 'ножиці')

        # This game named "Rock, paper, scissors".
        # The computer chooses one of the items, and you, in turn, must choose the item that defeats it.
        # Rock beats scissors, scissors cut paper, paper wraps rock.
        print(story["112"][language]['text'])
        # make time sleep to allow the player to read all the text.
        if audio == 'no' or audio == 'ні':
            time.sleep(story["112"]['time'])
        # play each audio recordings.
        elif audio == 'yes' or audio == 'так':
            for voice in story["112"][language]['voice'].values():
                playsound(voice)
        while True:
            # computer make random choose among game_list.
            comp_choice = random.choice(game_list)

            # play audio recording.
            if audio == 'yes' or audio == 'так':
                playsound(story["113"][language]['voice'])
            # player writes his choice.
            # Please choose: (rock, paper or scissors)
            user_choice = input(story["113"][language]['text'])

            # make tuple with a computer's choice and a player's choice.
            choice = (comp_choice, user_choice)

            # using Pattern Matching
            match choice:
                # all draw combination in english or ukrainian.
                case ('rock', 'rock') | ('paper', 'paper') | ('scissors', 'scissors') |\
                     ('камінь', 'камінь') | ('папір', 'папір') | ('ножиці', 'ножиці'):
                    if language == "en":
                        print(f'Computer chose {comp_choice}. Draw. let\'s try again.')
                        if audio == 'no':
                            time.sleep(5)
                        elif audio == 'yes':
                            playsound('vvauthor_say51.wav')
                    elif language == "укр":
                        print(f'Комп\'ютер обрав {comp_choice}. Нічия. Давайте спробуємо ще раз.')
                        if audio == 'ні':
                            time.sleep(5)
                        elif audio == 'так':
                            playsound('vrecord_ua124.wav')

                # all win combination in english or ukrainian.
                case ('rock', 'paper') | ('paper', 'scissors') | ('scissors', 'rock') |\
                     ('камінь', 'папір') | ('папір', 'ножиці') | ('ножиці', 'камінь'):
                    if language == "en":
                        print(f'Computer chose {comp_choice}. Congratulations. You win.'
                              f'\nLives have left {self._health}.')
                        if audio == 'no':
                            time.sleep(9)
                        elif audio == 'yes':
                            playsound('vvauthor_say52.wav')
                    elif language == "укр":
                        print(f'Комп\'ютер обрав {comp_choice}. Мої вітання. Ви перемогли.'
                              f'\nЖиттів залишилося {self._health}.')
                        if audio == 'ні':
                            time.sleep(9)
                        elif audio == 'так':
                            playsound('vrecord_ua125.wav')
                    time.sleep(1)
                    break

                # all loose combination in english or ukrainian.
                case ('rock', 'scissors') | ('paper', 'rock') | ('scissors', 'paper') |\
                     ('камінь', 'ножиці') | ('папір', 'камінь') | ('ножиці', 'папір'):
                    self._health -= 1       # One life will take away.
                    if language == "en":
                        print(f'Computer chose {comp_choice}. Computer wins. Health - 1.'
                              f'\nLives have left {self._health}.')
                        if audio == 'no':
                            time.sleep(9)
                        elif audio == 'yes':
                            playsound('vvauthor_say53.wav')
                    elif language == "укр":
                        print(f'Комп\'ютер обрав {comp_choice}. Комп\'ютер переміг. Ви втратили одне життя.'
                              f'\nЖиттів залишилося {self._health}.')
                        if audio == 'ні':
                            time.sleep(9)
                        elif audio == 'так':
                            playsound('vrecord_ua126.wav')

            # if lives ends it will raise the exception.
            if self._health == 0:
                raise Health_exception(self._health)

    # function to ask the question1.
    def hard_question1(self, language: str, audio: str):
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
                self._health -= 1  # One life will take away.
                if self._health == 0:  # if lives ends it will raise the exception.
                    raise Health_exception(self._health)
                # wrong answer the question in english or ukrainian.
                if language == "en":
                    print(f'\nNo, please think and answer again.\nLives have left {self._health}.')
                elif language == "укр":
                    print(f'\nНі, будь ласка, подумайте і дайте відповідь ще раз.\nЖиттів залишилося {self._health}.')
                if audio == 'yes' or audio == 'так':
                    playsound(story["105"][language]['voice'])
                # call function hard_question1 again.
                self.hard_question1(language, audio)

    # function to ask the question2.
    def hard_question2(self, language: str, audio: str):
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
                self._health -= 1           # One life will take away.
                if self._health == 0:       # if lives ends it will raise the exception.
                    raise Health_exception(self._health)
                # wrong answer the question in english or ukrainian.
                if language == "en":
                    print(f'\nNo, please think and answer again.\nLives have left {self._health}.')
                elif language == "укр":
                    print(f'\nНі, будь ласка, подумайте і дайте відповідь ще раз.\nЖиттів залишилося {self._health}.')
                if audio == 'yes' or audio == 'так':
                    playsound(story["105"][language]['voice'])
                # call function hard_question2 again.
                self.hard_question2(language, audio)

    # function to ask the question3.
    def hard_question3(self, language: str, audio: str):
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
                self._health -= 1           # One life will take away.
                if self._health == 0:       # if lives ends it will raise the exception.
                    raise Health_exception(self._health)
                # wrong answer the question in english or ukrainian.
                if language == "en":
                    print(f'\nNo, please think and answer again.\nLives have left {self._health}.')
                elif language == "укр":
                    print(f'\nНі, будь ласка, подумайте і дайте відповідь ще раз.\nЖиттів залишилося {self._health}.')
                if audio == 'yes' or audio == 'так':
                    playsound(story["105"][language]['voice'])
                # call function hard_question3 again.
                self.hard_question3(language, audio)

    # function to ask the question4.
    def hard_question4(self, language: str, audio: str):
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
                self._health -= 1           # One life will take away.
                if self._health == 0:       # if lives ends it will raise the exception.
                    raise Health_exception(self._health)
                # wrong answer the question in english or ukrainian.
                if language == "en":
                    print(f'\nNo, please think and answer again.\nLives have left {self._health}.')
                elif language == "укр":
                    print(f'\nНі, будь ласка, подумайте і дайте відповідь ще раз.\nЖиттів залишилося {self._health}.')
                if audio == 'yes' or audio == 'так':
                    playsound(story["105"][language]['voice'])
                # call function hard_question4 again.
                self.hard_question4(language, audio)
