# Імпортує модулі:
#       random - для створення випадкових чисел,
#       time - для сну комп'ютера.
#       Health_exception - якщо гравець втратив усі життя відбувається помилка,
#       playsound - для відкриття аудіо файлів.
import random
import time
from health_exception import Health_exception
from playsound import playsound


# клас Hard для відстеження кількості життів.
class Hard:

    def __init__(self):
        self._health = 10       # вказує, що у персонажа 10 життів.
        self.DICE_ART = {       # створює більш елегантні картинки для гри "Кидання кубиків".
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

    # Перша гра "Вгадай число".
    def game1(self):
        print('\nЦя гра називається "Вгадай число".\nКомп\'ютер загадав число від 1 до 10...')
        playsound('vrecord_ua110.wav')      # відкриваємо аудіо файл.
        clue = 1            # створює кількість підказок, щоб потім давати їх у грі.
        number = 7          # комп'ютер загадав число 7, бо торговий центр згорів 7-го червня.
        playsound('vrecord_ua111.wav')
        num = int(input('\nОбери число (від 1 до 10): '))
        all_num = set()     # створює множину, яке не показує повторювані числа.
        while num != number:        # створює while цикл, щоб перевірити чи дорівнює ваше число з загаданим числом.
            self._health -= 1       # якщо гравець не вгадав число, то забирається одне життя.
            if self._health == 0:   # якщо закінчились усі життя, відбувається виключення.
                raise Health_exception(self._health)
            all_num.add(num)        # додає попередні обрані числа.
            print(f'\nОй... Не вгадав!\nВи втратили одне життя.\nУ вас залишилося життів {self._health}.')
            playsound('vrecord_ua112.wav')
            if clue == 1:           # дає першу підказку
                print('\nЯ дам тобі одну підказку.\nЦе число більше 5.')
                playsound('vrecord_ua113.wav')
            elif clue == 2:         # дає другу підказку
                print('\nЩе одна підказка. Це непарне число.')
                playsound('vrecord_ua114.wav')
            print(f'\n(Ти вже обрав {sorted(set(all_num))})')
            playsound('vrecord_ua111.wav')
            num = int(input('Обери число (від 1 до 10): '))
            clue += 1       # щоб показати одну підказку в одному колі і другу підказку в іншому.
        else:               # якщо число гравця дорівнює числу, що загадав комп'ютер, то ви перемогли.
            print(f'\nМої вітання, ви перемогли!!!\nУ вас залишилося життів {self._health}.')
            playsound('vrecord_ua115.wav')
            time.sleep(1)
            return 1

    # Друга гра "Кидання кубиків".
    def game2(self):
        print('\nЦя гра називається "Кидання кубиків".'
              '\nВи повинні кинути кубики так, щоб сума цифр була більшою або дорівнювала 8.')
        playsound('vrecord_ua116.wav')
        playsound('vrecord_ua117.wav')
        playsound('vrecord_ua118.wav')
        input('\nБудь ласка напишіть слово "кинути". ')

        # генерує список для випадкових чисел.
        rand_choice = []
        # додає до списку випадковий вибір чисел завдяки модулю random.
        for i in range(2):
            rand_choice.append(random.randint(1, 6))
        while True:
            # генерує список з ключами картинок зі списку DICE_ART.
            dice_faces = []
            for value in rand_choice:
                dice_faces.append(self.DICE_ART[value])

            # генерує список, у якому містяться картинки з кістками.
            dice_faces_rows = []
            for row_idx in range(self.DICE_HEIGHT):
                row_components = []
                for die in dice_faces:
                    row_components.append(die[row_idx])
                row_string = self.DICE_FACE_SEPARATOR.join(row_components)
                dice_faces_rows.append(row_string)

            # генерує назву "Результат" посередині.
            width = len(dice_faces_rows[0])
            diagram_header = " RESULTS ".center(width, "~")

            # diagram_header приєднуємо до dice_faces_rows.
            dice_face_diagram = "\n".join([diagram_header] + dice_faces_rows)
            print(f"\n{dice_face_diagram}")

            # Перевіряє чи сума цифр більша або дорівнює 8.
            if (rand_choice[0] + rand_choice[1]) >= 8:
                print(f"Ви перемогли. Життів залишилося {self._health}.")
                playsound('vrecord_ua119.wav')
                time.sleep(1)
                break

            # якщо ні — то забирається одне життя.
            self._health -= 1
            print(f'Погана вдача. Життів залишилося {self._health}.')
            playsound('vrecord_ua120.wav')

            # якщо закінчились усі життя, відбувається виключення.
            if self._health == 0:
                raise Health_exception(self._health)

            # і знову генерує список для випадкових чисел.
            playsound('vrecord_ua118.wav')
            input('\nБудь ласка напишіть слово "кинути". ')
            rand_choice = []
            for i in range(2):
                rand_choice.append(random.randint(1, 6))
        return 1

    # Третя гра "Камінь, ножиці, папір".
    def game3(self):
        # створення кортежу з трьох варіантів "камінь", "папір" або "ножиці".
        game_list = ('камінь', 'папір', 'ножиці')
        print('\nЦя гра називається "Камінь, ножиці, папір".'
              '\nКомп\'ютер обирає один з варіантів, а ти, в свою чергу, повинен обрати той предмет який переможе його.'
              '\nКамінь б\'є ножиці, ножиці ріжуть папір, папір загортає камінь.')
        playsound('vrecord_ua121.wav')
        playsound('vrecord_ua122.wav')
        while True:
            # комп'ютер робить випадковий вибір серед game_list.
            comp_choice = random.choice(game_list)

            # гравець обирає свій предмет.
            playsound('vrecord_ua123.wav')
            user_choice = input('\nБудь ласка оберіть один із варіантів (камінь, ножиці, папір) ')

            # створення кортежу з вибором комп'ютера та гравця.
            choice = (comp_choice, user_choice)

            # використання Pattern Matching.
            match choice:
                # усі нічийні комбінації.
                case ('камінь', 'камінь') | ('папір', 'папір') | ('ножиці', 'ножиці'):
                    print(f'Комп\'ютер обрав {comp_choice}. Нічия. Давайте спробуємо ще раз.')
                    playsound('vrecord_ua124.wav')

                # усі переможні комбінації.
                case ('камінь', 'папір') | ('папір', 'ножиці') | ('ножиці', 'камінь'):
                    print(f'Комп\'ютер обрав {comp_choice}. Мої вітання. Ви перемогли.'
                          f'\nЖиттів залишилося {self._health}.')
                    playsound('vrecord_ua125.wav')
                    time.sleep(1)
                    break

                # усі програшні комбінації.
                case ('камінь', 'ножиці') | ('папір', 'камінь') | ('ножиці', 'папір'):
                    self._health -= 1   # забирається одне життя.
                    print(f'Комп\'ютер обрав {comp_choice}. Комп\'ютер переміг. Ви втратили одне життя.'
                          f'\nЖиттів залишилося {self._health}.')
                    playsound('vrecord_ua126.wav')

            # якщо закінчились усі життя, відбувається виключення.
            if self._health == 0:
                raise Health_exception(self._health)

    # функція для відповіді на питання 1.
    def choice3(self):
        choice3 = input('Ви думаєте що це був ')
        # якщо відповідь не дорівнює "Майк" або "Майк Вільямс" знову повторює питання.
        # використовує функцію title, щоб зробити великою першу літеру.
        while choice3.title() != 'Майк' and choice3.title() != 'Майк Вільямс':
            self._health -= 1           # забирається одне життя.
            if self._health == 0:       # якщо закінчились усі життя, відбувається виключення.
                raise Health_exception(self._health)
            print(f'\nНі, будь ласка, подумайте і дайте відповідь ще раз.\nЖиттів залишилося {self._health}.')
            playsound('vrecord_ua86.wav')
            playsound('vrecord_ua85.wav')
            choice3 = input('\nХто підпалив торговельний центр? ')

    # функція для відповіді на питання 2.
    def choice4(self):
        choice4 = input('Ви думаєте що він обпік ')
        # якщо відповідь не дорівнює "руки" або "рука" знову повторює питання.
        # використовує функцію lower, щоб зробити слово з маленьких літер.
        while choice4.lower() != 'руки' and choice4.lower() != 'руку':
            self._health -= 1           # забирається одне життя.
            if self._health == 0:       # якщо закінчились усі життя, відбувається виключення.
                raise Health_exception(self._health)
            print(f'\nНі, будь ласка, подумайте і дайте відповідь ще раз.\nЖиттів залишилося {self._health}.')
            playsound('vrecord_ua86.wav')
            playsound('vrecord_ua89.wav')
            choice4 = input('\nЯка частина тіла Майка згоріла? ')

    # функція для відповіді на питання 3.
    def choice5(self):
        choice5 = input('Ви думаєте що це ')
        # якщо відповідь не дорівнює "7" знову повторює питання.
        while choice5 != '7':
            self._health -= 1           # забирається одне життя.
            if self._health == 0:       # якщо закінчились усі життя, відбувається виключення.
                raise Health_exception(self._health)
            print(f'\nНі, будь ласка, подумайте і дайте відповідь ще раз.\nЖиттів залишилося {self._health}.')
            playsound('vrecord_ua86.wav')
            playsound('vrecord_ua92.wav')
            choice5 = input('\nЯкого червня сталася пожежа? (число) ')

    # функція для відповіді на питання 4.
    def choice6(self):
        choice6 = input('Ви думаєте його ')
        # якщо відповідь не дорівнює "отруїли" знову повторює питання.
        # використовує функцію lower, щоб зробити слово з маленьких літер.
        while choice6.lower() != 'отруїли':
            self._health -= 1           # забирається одне життя.
            if self._health == 0:       # якщо закінчились усі життя, відбувається виключення.
                raise Health_exception(self._health)
            print(f'\nНі, будь ласка, подумайте і дайте відповідь ще раз.\nЖиттів залишилося {self._health}.')
            playsound('vrecord_ua86.wav')
            playsound('vrecord_ua94.wav')
            choice6 = input('\nЯк вбили Майка? (застрелили, зарізали чи отруїли) ')
