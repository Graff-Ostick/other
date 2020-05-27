import random

print('-------------------------------------------')
print('---------Rock, paper, scissors-------------')
print('--------Welcome to the game!---------------')
print('-----the game consist of three rounds.-----')
print('The winner is the one who score more points')

print('\t [r] - rock\n\t [s] - scissors\n\t [p] - paper')



player_score = 0
player_select = 0
comp_score = 0
comp_select = 0

print('------------------------------------------')
print('--------------Start the Game--------------')

for i in range(3):
    print('\t------------Round № ' +str(i+1) +'-------------')
    comp_select = random.choice('rps')

    while True:
        player_select = input("Enter your choice: ")
        if player_select == 'r' \
        or player_select == 'p' \
        or player_select == 's':
            break
        else:
            print('Error, try again')


    print('\t Compure choice : '+comp_select)

    if player_select == comp_select:
        print('\tDraw!')
    elif player_select == 'r' and comp_select == 's':
        player_score +=1
        print('\tYou win!')
    elif player_select == 's' and comp_select == 'p':
        player_score +=1
        print('\tYou win!')
    elif player_select == 'p' and comp_select == 'r':
        player_score +=1
        print('\tYou win!')

    elif player_select == 'p' and comp_select == 's':
        comp_score +=1
        print('\tThe computer win')
    elif player_select == 's' and comp_select == 'r':
        comp_score +=1
        print('\tThe computer win')
    elif player_select == 'r' and comp_select == 'p':
        comp_score +=1
        print('\tThe computer win')

print('------------------------------------------')
print('---------------GAME RESULT----------------')

if player_score>comp_score:
    print("Congratulations! You finaly win")
elif comp_score>player_score:
    print('Sorry =( the computer wins! ')
else:
    print("Draw!")
