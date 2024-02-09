def game_state(table):
  lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], 
          [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
  
  for line in lines:
    if table[line[0]] == table[line[1]] and table[line[1]] == table[line[2]] and table[line[0]] != '.':
      return player_token(table[line[0]])
  
  if '.' in table:
    return 'continue'
  
  return 0

def player_token(token: str) -> int:
  if token == 'x':
    return 1
  
  else:
    return -1
           