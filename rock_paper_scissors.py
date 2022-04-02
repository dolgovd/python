import random

userWins = 0
computerWins = 0
options =  ['rock', 'paper', 'scissors']

while True:
    userInput = input('Please select (Rock, Paper, Scissors) or enter Q to quit: ').lower()
    if userInput == 'q':
        break

    if userInput not in options:
        continue
    
    randomNumber = random.randint(0, 2)
    # rock : 0, paper : 1, scissors : 2
    computerPick = options[randomNumber]
    print('Computer picked: ', computerPick + '.')

    if userInput == 'rock' and computerPick == 'scissors':
        print('You won!')
        userWins += 1
        
    elif userInput == 'paper' and computerPick == 'rock':
        print('You won!')
        userWins += 1
        
    elif userInput == 'scissors' and computerPick == 'paper':
        print('You won!')
        userWins += 1
    
    elif userInput == 'rock' and computerPick == 'rock':
        print('No one wins')
    
    elif userInput == 'paper' and computerPick == 'paper':
        print('No one wins')
    
    elif userInput == 'scissors' and computerPick == 'scissors':
        print('No one wins')

    else:
        print('You lost!')
        computerWins += 1
    
print('You won', userWins, 'times')
print('Computer won', computerWins, 'times')
print('See you later!')