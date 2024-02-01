import json

from models.player import Player

class Tournament:
    def __init__(self, name, place, start_date, end_date, description, players_list):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        
        self.players_list = []
        for player in players_list:
            player_group = Player(name=player["name"],
                                  surname=player["surname"],
                                  chess_id=player["chess_id"],
                                  date_of_birth=player["date_of_birth"],
                                  score=player["score"])
            self.players_list.append(player_group)

    def __str__(self):
        return f"{self.name}, du {self.start_date} au {self.end_date}"
    
    @staticmethod    
    def save_tournament_to_json(tournament_data):
        with open("data/tournament_list.json", "a") as json_file:
            json.dump(tournament_data, json_file)
            json_file.write('\n')

    @classmethod    
    def load_tournaments_from_json(cls, file_path):
        all_tournaments = []
        with open(file_path, "r") as json_file:
            for line in json_file:
                tournament_data = json.loads(line)
                
                tournament = cls(
                    name=tournament_data['name'],
                    place=tournament_data['place'],
                    start_date=tournament_data['start_date'],
                    end_date=tournament_data['end_date'],
                    description=tournament_data['description'],
                    players_list=tournament_data['players_list'])
                
                all_tournaments.append(tournament)

        print("\nListe des joueurs:\n")
        for tournament in all_tournaments:
            print(f"{tournament}\n")

file_path = "/Users/guwoop/Documents/chess_tournament/data/tournament_list.json"