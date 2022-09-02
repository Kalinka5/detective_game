import random
from health_exception import Health_exception
import time


class Hard_ua:

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
        print('\nЦя гра називається "Вгадай число".\nКомп\'ютер загадав число від 1 до 10...')
        time.sleep(6)
        clue = 1
        number = 7
        num = int(input('\nОбери число (від 1 до 10): '))
        all_num = set()
        while num != number:
            self._health -= 1
            if self._health == 0:
                raise Health_exception(self._health)
            all_num.add(num)
            print(f'\nОй... Не вгадав!\nВи втратили одне життя.\nУ вас залишилося життів {self._health}.')
            time.sleep(6)
            if clue == 1:
                print('\nЯ тобі дам одну підказку.\nЦе число більше 5.')
                time.sleep(4)
            elif clue == 2:
                print('\nЩе одна підказка. Це непарне число.')
                time.sleep(4)
            print(f'\n(Ти вже обрав {sorted(set(all_num))})')
            num = int(input('Обери число (від 1 до 10): '))
            clue += 1
        else:
            print(f'\nМої вітання, ви перемогли!!!\nУ вас залишилося життів {self._health}.')
            time.sleep(6)
            return 1

    def game2(self):
        print('\nЦя гра називається "Кидання кубиків".'
              '\nВи повинні кинути кубики так, щоб сума цифр була більшою або дорівнювала 8.')
        time.sleep(12)
        input('\nБудь ласка напишіть слово "кинути". ')
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
            diagram_header = " Результат ".center(width, "~")

            dice_face_diagram = "\n".join([diagram_header] + dice_faces_rows)

            print(f"\n{dice_face_diagram}")
            if (rand_choice[0] + rand_choice[1]) >= 8:
                print(f"Ви перемогли. Життів залишилося {self._health}.")
                time.sleep(5)
                break
            self._health -= 1
            print(f'Погана вдача. Життів залишилося {self._health}.')
            time.sleep(4)
            if self._health == 0:
                raise Health_exception(self._health)
            input('\nБудь ласка напишіть слово "кинути". ')
            rand_choice = []
            for i in range(2):
                rand_choice.append(random.randint(1, 6))
        return 1

    def game3(self):
        game_list = ('камінь', 'папір', 'ножиці')
        print('\nЦя гра називається "Камінь, ножиці, папір".'
              '\nКомп\'ютер обирає один з варіантів, а ти, в свою чергу, повинен обрати той предмет який переможе його.'
              '\nКамінь б\'є ножиці, ножиці ріжуть папір, папір загортає камінь.')
        time.sleep(17)
        while True:
            comp_choice = random.choice(game_list)
            user_choice = input('\nБудь ласка оберіть один із варіантів (камінь, ножиці, папір) ')
            choice = (comp_choice, user_choice)
            match choice:
                case ('камінь', 'камінь') | ('папір', 'папір') | ('ножиці', 'ножиці'):
                    print(f'Комп\'ютер обрав {comp_choice}. Нічия. Давайте спробуємо ще раз.')
                    time.sleep(5)
                case ('камінь', 'папір') | ('папір', 'ножиці') | ('ножиці', 'камінь'):
                    print(f'Комп\'ютер обрав {comp_choice}. Мої вітання. Ви перемогли.'
                          f'\nЖиттів залишилося {self._health}.')
                    time.sleep(8)
                    break
                case ('камінь', 'ножиці') | ('папір', 'камінь') | ('ножиці', 'папір'):
                    self._health -= 1
                    print(f'Комп\'ютер обрав {comp_choice}. Комп\'ютер переміг. Ви втратили одне життя.'
                          f'\nЖиттів залишилося {self._health}.')
                    time.sleep(8)
            if self._health == 0:
                raise Health_exception(self._health)

    def choice3(self):
        choice3 = input('Ви думаєте що це був ')
        while choice3.title() != 'Майк' and choice3.title() != 'Майк Вільямс':
            self._health -= 1
            if self._health == 0:
                raise Health_exception(self._health)
            print(f'\nНі, будь ласка, подумайте і дайте відповідь ще раз.\nЖиттів залишилося {self._health}.')
            choice3 = input('\nХто підпалив торговельний центр? ')

    def choice4(self):
        choice4 = input('Ви думаєте що він обпік ')
        while choice4.lower() != 'руки' and choice4.lower() != 'рука':
            self._health -= 1
            if self._health == 0:
                raise Health_exception(self._health)
            print(f'\nНі, будь ласка, подумайте і дайте відповідь ще раз.\nЖиттів залишилося {self._health}.')
            choice4 = input('\nЯка частина тіла Майка згоріла? ')

    def choice5(self):
        choice5 = input('Ви думаєте що це ')
        while choice5 != '7':
            self._health -= 1
            if self._health == 0:
                raise Health_exception(self._health)
            print(f'\nНі, будь ласка, подумайте і дайте відповідь ще раз.\nЖиттів залишилося {self._health}.')
            choice5 = input('\nЯкого червня сталася пожежа?(число) ')

    def choice6(self):
        choice6 = input('Ви думаєте його ')
        while choice6.lower() != 'отруїли':
            self._health -= 1
            if self._health == 0:
                raise Health_exception(self._health)
            print(f'\nНі, будь ласка, подумайте і дайте відповідь ще раз.\nЖиттів залишилося {self._health}.')
            choice6 = input('\nЯк вбили Майка (пострілом, зарізали чи отруїли) ')
