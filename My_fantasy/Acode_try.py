



class Player:
  def __init__(self, hp: int):
    self.hp = hp
    
  
  
  
  
  
def input_settings():
  try:
    hp_val = int(input("Input your hp: " ))
    player = Player(hp_val)
    return f"Your hp: {player.hp}"
  except Exception as e:
    return f"Error {e}, pleace try latter."
    
    
    
print(input_settings())