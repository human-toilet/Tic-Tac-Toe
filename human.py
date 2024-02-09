class Human:
  def __init__(self, name):
    self.__name = name
  
  def play(self, table):
    while True:
      choice = input('Ingress your play\n')

      try:
        number = int(choice)
        
        if table[number] == '.':
          table[number] = '0'
          return table
        
        else:
          print('Ingress a valid option')
      
      except:
        print('Ingress a valid option')
        
  @property
  def name(self):
    return self.__name