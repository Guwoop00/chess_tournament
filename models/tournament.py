class Tournament:
    def __init__(self, name, place, start_date, end_date, description, players_in_tournament):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.description = description        
        self.players_in_tournament = players_in_tournament


    def __str__(self):
        return f"{self.name}, du {self.start_date} au {self.end_date}"