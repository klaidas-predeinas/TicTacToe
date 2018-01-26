positions = {}

for i in range(1,10):
    positions[i] = ' '

print(positions)

def draw():
    for b in range(1,10):
        if b % 3 != 0:
            print(' '+positions[b]+' '+'|', end='')
        else:
            print(' '+positions[b]+' ', end='')
        if b == 3 or b == 6:
            print('\n '+'~ '*5)

def win(positions):
    #player1
    for i in range(1,10,3):
        if positions[i] == 'x' and positions[i+1] == 'x' and positions[i+2] == 'x':
            return '\nPlayer1 Is the Winner'
    for i in range(1,4):
        if positions[i] == 'x' and positions[i+3] == 'x' and positions[i+6] == 'x':
            return '\nPlayer1 Is the Winner'
    if positions[1] == 'x' and positions[5] == 'x' and positions[9] == 'x':
        return '\nplayer1 is the winner'
    elif positions[3] == 'x' and positions[5] == 'x' and positions[7] == 'x':
        return '\nplayer1 is the winner'

    #player2
    for i in range(1,10,3):
        if positions[i] == 'o' and positions[i+1] == 'o' and positions[i+2] == 'o':
            return '\nPlayer1 Is the Winner'
    for i in range(1,4):
        if positions[i] == 'o' and positions[i+3] == 'o' and positions[i+6] == 'o':
            return '\nPlayer1 Is the Winner'
    if positions[1] == 'o' and positions[5] == 'o' and positions[9] == 'o':
        return '\nplayer1 is the winner'
    elif positions[3] == 'o' and positions[5] == 'o' and positions[7] == 'o':
        return '\nplayer1 is the winner'

draw()

Player1 = 'x'
Player2 = 'o'

for i in range(5):
  if win(positions) != None:
    print(win(positions))
    break

  positions[int(input('\n(P1)Choose a number between 1-9(which is not taken), to put your "X" down: '))] = Player1
  draw()

  if win(positions) != None:
    print(win(positions))
    break

  if i != 4:
      positions[int(input('\n(P2)Choose a number between 1-9(which is not taken), to put your "O" down: '))] = Player2
      draw()
