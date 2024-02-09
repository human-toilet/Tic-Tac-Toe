def copy(table: list) -> list:
  new_table = []
  
  for element in table:
    new_table.append(element)
  
  return new_table

def min_list(list: list) -> int:
  aux = 2
  
  for element in list:
    if element < aux:
      aux = element
  
  return aux

def max_list(list: list) -> int:
  aux = -2
  
  for element in list:
    if element > aux:
      aux = element
  
  return aux
