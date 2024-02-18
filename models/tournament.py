from datetime import datetime

class Tournament:
    def __init__(self, name, place, end_date, description, players_in_tournament, start_date=datetime.now().strftime(f"à %H:%M:%S le %d-%m-%Y"), total_rounds=4):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.description = description        
        self.players_in_tournament = players_in_tournament
        self.total_rounds = total_rounds


    def __str__(self):
        return f"{self.name}, du {self.start_date} au {self.end_date}"
    
    def __repr__(self):
        return f"{self.name}, du {self.start_date} au {self.end_date}"
    
    def to_dict(self):
        return {
            'name': self.name,
            'place': self.place,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'description': self.description,
            'players_in_tournament': self.players_in_tournament,
            'total_rounds': self.total_rounds
        }