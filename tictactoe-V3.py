def draw():
    #used to draw out the grid, in the format of a tictactoe game.
    for b in range(1,10):
        if b % 3 != 0:
            print(' '+positions[b]+' '+'|', end='')
        else:
            print(' '+positions[b]+' ', end='')
        if b == 3 or b == 6:
            print('\n '+'~ '*5)

def win(positions):
    #player1
    #checks if player 1 is the winner
    for i in range(1,10,3):
        #horizontal
        if positions[i] == 'x' and positions[i+1] == 'x' and positions[i+2] == 'x':
            return '\nPlayer1 Is the Winner'
    for i in range(1,4):
        #vertical
        if positions[i] == 'x' and positions[i+3] == 'x' and positions[i+6] == 'x':
            return '\nPlayer1 Is the Winner'
    #diagonal
    if positions[1] == 'x' and positions[5] == 'x' and positions[9] == 'x':
        return '\nPlayer1 is the winner'
    elif positions[3] == 'x' and positions[5] == 'x' and positions[7] == 'x':
        return '\nPlayer1 is the winner'

    #player2
    #checks if player 2 is the winner
    for i in range(1,10,3):
        #horizontal
        if positions[i] == 'o' and positions[i+1] == 'o' and positions[i+2] == 'o':
            return '\nPlayer2 Is the Winner'
    for i in range(1,4):
        #vertical
        if positions[i] == 'o' and positions[i+3] == 'o' and positions[i+6] == 'o':
            return '\nPlayer2 Is the Winner'
    #diagonal
    if positions[1] == 'o' and positions[5] == 'o' and positions[9] == 'o':
        return '\nPlayer2 is the winner'
    elif positions[3] == 'o' and positions[5] == 'o' and positions[7] == 'o':
        return '\nPlayer2 is the winner'

Player1 = 'x'
Player2 = 'o'
p1Score = 0
p2Score = 0

#makes it show that there is 3 games
for i in range(3):
    positions = {}

    # creates a dictionary that is numbered 1-9 with each valued equal to ' '
    for i in range(1, 10):
        positions[i] = ' '

    draw()
    #repeats this code 5 times, this will fill the whole grid, if there is no winner
    for i in range(5):
        #this checks if there is a winner, if there isn't a winner it will return 'none' which wont run this code below
        if win(positions) != None:
            print(win(positions))
            #if it returns player1 is ther winner, it will add a score to player1 else player2 gains a score
            if 'Player1' in win(positions):
                p1Score += 1
            else:
                p2Score += 1
            break
        #ask user to put there x on the grid, this will automatically put it in the dictionary which will then be printed out via draw()
        while True:
            pos = int(input('\n(P1)Choose a number between 1-9(which is not taken), to put your "X" down: '))
            if positions[pos] == ' ':
                positions[pos] = Player1
                break
            else:
                print('position is already taken please try again')
        draw()

        #this checks again, incase there is a winner after the previous input.
        if win(positions) != None:
            print(win(positions))
            # if it returns player1 is ther winner, it will add a score to player1 else player2 gains a score
            if 'Player1' in win(positions):
                p1Score += 1
            else:
                p2Score += 1
            break

        #an if statement which makes sure there isn't an extra value that is inputted into the grid since it repeats 5 times and theres 2 players so there would be an overall of 10 placements which is not needed.
        if i != 4:
            while True:
                pos = int(input('\n(P1)Choose a number between 1-9(which is not taken), to put your "o" down: '))
                if positions[pos] == ' ':
                    positions[pos] = Player2
                    break
                else:
                    print('position is already taken please try again')
            draw()

#checks if player1 or player2 won the game, and prints the score out.
if p1Score > p2Score:
    print('player 1 is the winner with the score of p1:p2 - {}'.format((str(p1Score)+':'+str(p2Score))))
else:
    print('player 2 is the winner with the score of p1:p2 - {}'.format((str(p1Score) + ':' + str(p2Score))))