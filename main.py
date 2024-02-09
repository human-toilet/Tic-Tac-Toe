from ia import IA
from table import print_table, INITIAL_TABLE
from human import Human
from rules import game_state
import os

def start():
  name = input("Ingress your name and press 'enter' to continue\n")
  player1 = Human(name)
  player2 = IA()
  players = [player1, player2]
  i = 0
  init = INITIAL_TABLE

  while True:
    os.system('clear')
    aux = game_state(init)
    
    if aux!= 0 and aux != 'continue':
      print(f'{players[int(not i)].name} wins!')
      print_table(init)
      break
    
    elif aux == 0:
      print('Game Over')
      print_table(init)
      break
       
    print(f"It is {players[i].name}'s turn")
    print_table(init)
    spacy = input("Press 'enter' to continue") 
    init = players[i].play(init)
    i += 1

    if i == 2: 
      i = 0

#start()


