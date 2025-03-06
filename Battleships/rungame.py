import ship
import game
restart = ''
while restart != 'no':
    game.play_game(12)

    restart = input('Would you like to play again?(yes/no): ')
    if restart.lower() == 'no':
        print('Thanks for playing')
        break
    else:
        continue