nowinner = True

while nowinner:
    p1go = input('Player 1 go: ')
    p2go = input('Player 2 go: ')
    if (p1go == 'Rock' and p2go == 'Scissors') or (p1go == 'Scissors' and p2go == 'Paper') or (p1go == 'Paper' and p2go == 'Rock'):
        print ('Player 1 wins!')
        break
    elif (p2go == 'Rock' and p1go == 'Scissors') or (p2go == 'Scissors' and p1go == 'Paper') or (p2go == 'Paper' and p1go == 'Rock'):
        print ('Player 2 wins!')
        break
    elif p2go == p1go:
        print ('It is a tie! Keep playing...')
        