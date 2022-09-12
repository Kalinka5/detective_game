# import module game - full console game.
from game import game


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
        # call function of detective game.
        game(language)
