from rules import game_state
from utils import copy, min_list, max_list
from table import print_table

class IA:
  def __init__(self):
    self.__name = 'bot_hard'
    
  def play(self, table: list) -> list:
    tables = self.__gen_tables(table, 'x')
    table_value = list(map(self.__play_max, tables))
    return tables[table_value.index(max_list(table_value))]
    
  def __gen_tables(self, table: list, token: str) -> list:
    aux: list = []
    
    for i in range(len(table)):
      if table[i] == '.':
        gen = copy(table)
        gen[i] = token
        aux.append(gen)

    return aux
  
  def __play_max(self, table) -> int:
    aux = game_state(table)
    
    if aux != 'continue':
      return aux
    
    tables = self.__gen_tables(table, '0')
    table_value = list(map(self.__play_min, tables))
    return min_list(table_value)
    
  def __play_min(self, table) -> int:
    aux = game_state(table)
    
    if aux != 'continue':
      return aux
    
    tables = self.__gen_tables(table, 'x')
    tabe_value = list(map(self.__play_max, tables))
    return max_list(tabe_value)

  @property
  def name(self):
    return self.__name 

"""
def test():
  player = IA()
  print_table(player.play(['x', '.', '.',
                           '.', '0', '.',
                           '.', '.', '0']))

test()
"""