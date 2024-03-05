from datetime import datetime


class Tournament:
    def __init__(
        self,
        name,
        place,
        description,
        players_in_tournament,
        start_date=datetime.now().strftime("%H:%M:%S le %d-%m-%Y"),
        end_date=None,
        total_rounds=4,
        current_round=1,
        rounds=[],
        pairs_history=[],
    ):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.players_in_tournament = players_in_tournament
        self.total_rounds = total_rounds
        self.current_round = current_round
        self.rounds = rounds
        self.pairs_history = pairs_history

    def __str__(self):
        return f"{self.name}, du {self.start_date} au {self.end_date}"

    def __repr__(self):
        return f"{self.name}, du {self.start_date} au {self.end_date}"

    def to_json(self):
        """
        Convert tournament data to a dictionary.

        Returns:
            dict: Dictionary containing tournament data.
        """
        return {
            "name": self.name,
            "place": self.place,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "total_rounds": self.total_rounds,
            "current_round": self.current_round,
            "players_in_tournament": self.players_in_tournament,
            "rounds": self.rounds,
            "pairs_history": self.pairs_history,
        }
