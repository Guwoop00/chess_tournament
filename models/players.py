from dataclasses import dataclass

@dataclass
class Player:
    name: str
    surname: str
    date_of_birth: str
    score: int = 0

    
moi = Player("Morgan", "Justine", "13/05/1991")
print(moi.date_of_birth)