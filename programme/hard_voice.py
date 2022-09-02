import random
import time

from health_exception import Health_exception
from playsound import playsound


class Hard:

    def __init__(self):
        self._health = 10
        self.DICE_ART = {
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

    def game1(self):
        print('\nThis game named "Guess the number".\nThe computer guessed a number from 1 to 10...')
        playsound('vvauthor_say54.wav')
        clue = 1
        number = 7
        playsound('vvauthor_say55.wav')
        num = int(input('\nChoose number (from 1 to 10): '))
        all_num = set()
        while num != number:
            self._health -= 1
            if self._health == 0:
                raise Health_exception(self._health)
            all_num.add(num)
            print(f'\nOhh... You`re loose!\nMinus 1 point.\nYou have left {self._health} lives.')
            playsound('vvauthor_say56.wav')
            if clue == 1:
                print('\nI\'ll give you a clue.\nThis number is greater than 5.')
                playsound('vvauthor_say57.wav')
            elif clue == 2:
                print('\nI\'ll give you one more clue.\nThis is odd number.')
                playsound('vvauthor_say58.wav')
            print(f'\n(You have chosen {sorted(all_num)})')
            playsound('vvauthor_say55.wav')
            num = int(input('Choose number(from 1 to 10): '))
            clue += 1
        else:
            print(f'\nCongratulations, you win!!!\nYou have left {self._health} lives.')
            playsound('vvauthor_say59.wav')
            time.sleep(1)
            return 1

    def game2(self):
        print('\nThis game named "Dice rolling".'
              '\nYou must roll the dice and the sum of the digits must be greater than or equal to 8.')
        playsound('vvauthor_say60.wav')
        playsound('vvauthor_say61.wav')
        input('\nPlease write word "throw". ')
        rand_choice = []
        for i in range(2):
            rand_choice.append(random.randint(1, 6))
        while True:
            # Generate a list of dice faces from DICE_ART
            dice_faces = []
            for value in rand_choice:
                dice_faces.append(self.DICE_ART[value])

            # Generate a list containing the dice faces rows
            dice_faces_rows = []
            for row_idx in range(self.DICE_HEIGHT):
                row_components = []
                for die in dice_faces:
                    row_components.append(die[row_idx])
                row_string = self.DICE_FACE_SEPARATOR.join(row_components)
                dice_faces_rows.append(row_string)

            # Generate header with the word "RESULTS" centered
            width = len(dice_faces_rows[0])
            diagram_header = " RESULTS ".center(width, "~")

            dice_face_diagram = "\n".join([diagram_header] + dice_faces_rows)

            print(f"\n{dice_face_diagram}")
            if (rand_choice[0] + rand_choice[1]) >= 8:
                print(f"You win. Lives have left {self._health}.")
                playsound('vvauthor_say62.wav')
                time.sleep(1)
                break
            self._health -= 1
            print(f'Bad luck. Lives have left {self._health}.')
            playsound('vvauthor_say63.wav')
            if self._health == 0:
                raise Health_exception(self._health)
            playsound('vvauthor_say61.wav')
            input('\nPlease write word "throw". ')
            rand_choice = []
            for i in range(2):
                rand_choice.append(random.randint(1, 6))
        return 1

    def game3(self):
        game_list = ('rock', 'paper', 'scissors')
        print('\nThis game named "Rock, paper, scissors".'
              '\nThe computer chooses one of the items, and you, in turn, must choose the item that defeats it. '
              '\nRock beats scissors, scissors cut paper, paper wraps rock.')
        playsound('vvauthor_say49.wav')
        while True:
            comp_choice = random.choice(game_list)
            playsound('vvauthor_say50.wav')
            user_choice = input('\nPlease choose: (rock, paper or scissors) ')
            choice = (comp_choice, user_choice)
            match choice:
                case ('rock', 'rock') | ('paper', 'paper') | ('scissors', 'scissors'):
                    print(f'Computer chose {comp_choice}. Draw. let\'s try again.')
                    playsound('vvauthor_say51.wav')
                case ('rock', 'paper') | ('paper', 'scissors') | ('scissors', 'rock'):
                    print(f'Computer chose {comp_choice}. Congratulations. You win.\nLives have left {self._health}.')
                    playsound('vvauthor_say52.wav')
                    time.sleep(1)
                    break
                case ('rock', 'scissors') | ('paper', 'rock') | ('scissors', 'paper'):
                    self._health -= 1
                    print(f'Computer chose {comp_choice}. Computer wins. Health - 1.\nLives have left {self._health}.')
                    playsound('vvauthor_say53.wav')
            if self._health == 0:
                raise Health_exception(self._health)

    def choice3(self):
        choice3 = input('You think it was ')
        while choice3.title() != 'Mike' and choice3.title() != 'Mike Williams':
            self._health -= 1
            if self._health == 0:
                raise Health_exception(self._health)
            print(f'\nNo, please think and answer again.\nLives have left {self._health}.')
            playsound('vvauthor_say38.wav')
            playsound('vvauthor_say37.wav')
            choice3 = input('\nWho set fire to the mall? ')
            
    def choice4(self):
        choice4 = input('You think he burned ')
        while choice4.lower() != 'hands' and choice4.lower() != 'hand' and choice4.lower() != 'arms':
            self._health -= 1
            if self._health == 0:
                raise Health_exception(self._health)
            print(f'\nNo, please think and answer again.\nLives have left {self._health}.')
            playsound('vvauthor_say38.wav')
            playsound('vvauthor_say40.wav')
            choice4 = input('\nWhat body part did Mike burn? ')
        
    def choice5(self):
        choice5 = input('You think it was June ')
        while choice5 != '7' and choice5.lower() != '7th':
            self._health -= 1
            if self._health == 0:
                raise Health_exception(self._health)
            print(f'\nNo, please think and answer again.\nLives have left {self._health}.')
            playsound('vvauthor_say38.wav')
            playsound('vvauthor_say41.wav')
            choice5 = input('\nWhat June did the fire happen? (number) ')

    def choice6(self):
        choice6 = input('You think he was ')
        while choice6.lower() != 'poisoned':
            self._health -= 1
            if self._health == 0:
                raise Health_exception(self._health)
            print(f'\nNo, please think and answer again.\nLives have left {self._health}.')
            playsound('vvauthor_say38.wav')
            playsound('vvauthor_say42.wav')
            choice6 = input('\nHow was Mike killed? (shot, stabbed or poisoned) ')
