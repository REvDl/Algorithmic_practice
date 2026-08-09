



class Player:
  def __init__(self, name: str | None = "Jane doe", hp: int | None = 100, icon: str | None = "*"):
    self.hp = hp
    self.name = name
    self.icon = icon
    
  
  
  
  
  
def input_settings():
  try:
    hp_val = int(input("Input your hp: " ))
    player = Player(hp=hp_val)
    return f"Your player: {player.hp, player.name, player.icon}"
  except Exception as e:
    return f"Error {e}, pleace try latter."
    
    
    
print(input_settings())