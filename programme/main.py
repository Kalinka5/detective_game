# import modules:
#       main_text - english text game.
#       main_voice - english voice-text game.
#       main_text_ua - ukrainian text game.
#       main_voice_ua - ukrainian voice-text game.
from text_game import main_text
from voice_game import main_voice
from text_game_ua import main_text_ua
from voice_game_ua import main_voice_ua


# run only main file.
if __name__ == '__main__':
    # player can choose language he/she is comfortable with.
    language = input('\nБудь ласка, введіть мову, яку вам зручно сприймати. (укр)'
                     '\nPlease enter the language you are comfortable with. (en) ')
    # if player enters not "en" or not "укр", it will repeat request.
    while language != 'en' and language != 'укр':
        print('\nYou didn\'t enter what you asked for!\nВи ввели не те, що просили!')
        language = input('\nБудь ласка, введіть мову, яку вам зручно сприймати. (укр)'
                         '\nPlease enter the language you are comfortable with. (en) ')
    else:
        if language == 'en':
            # player also can choose play game with audio or without it.
            audio = input('\nDo you want play game with voice? (yes or no) ')
            while audio != 'yes' and audio != 'no':
                print('You didn\'t enter what you asked for!')
                audio = input('\nDo you want play game with voice? (yes or no) ')
            else:
                if audio == 'yes':
                    main_voice()
                elif audio == 'no':
                    main_text()
        elif language == 'укр':
            # player can choose play game with audio or without it ukrainian.
            audio = input('\nВи бажаєте грати в гру з голосом? (так чи ні) ')
            while audio != 'так' and audio != 'ні':
                print('Ви ввели не те, що просили!')
                audio = input('\nВи бажаєте грати в гру з голосом? (так чи ні) ')
            else:
                if audio == 'так':
                    main_voice_ua()
                elif audio == 'ні':
                    main_text_ua()
