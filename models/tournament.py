class Tournament:
    def __init__(self, name, place, start_date, end_date, description, players_in_tournament, current_round=1, total_rounds=4):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.description = description        
        self.players_in_tournament = players_in_tournament
        self.current_round = current_round
        self.total_rounds = total_rounds


    def __str__(self):
        return f"{self.name}, du {self.start_date} au {self.end_date}"