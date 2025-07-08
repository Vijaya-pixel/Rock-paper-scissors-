import random

print('===================')
print('Rock Paper Scissors')
print('===================')
print('                   ')
print('1) Rock')
print('2) Paper')
print('3) Scissors')

player = int(input('Pick a number: '))
print('You chose: ' ,int(player))

computer = random.randint(1,3)
print('Computer chose ', int(computer))

if player == 1 and computer == 3:
  print('The player won!')
elif player == 2 and computer == 1:
  print('The player won!')
elif player ==3 and computer == 2:
  print('The player won!')
elif player == computer:
  print('Tie')
else:
  print('The computer won!')
