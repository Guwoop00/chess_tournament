import json

class Player:
    def __init__(self, name, surname, chess_id, date_of_birth, score=0):
        self.name = name
        self.surname = surname
        self.chess_id = chess_id
        self.date_of_birth = date_of_birth
        self.score = score

    def __str__(self):
        return f"{self.name} {self.surname} {self.chess_id} {self.date_of_birth}"
    
    def __repr__(self):
        return f"{self.name} {self.surname}\n{self.chess_id}\n{self.date_of_birth}\n" 

    @staticmethod
    def save_players_to_json(all_players):
        with open(file_path, "w") as json_file:
            for player in all_players:
                player_dict = {
                    'name': player.name,
                    'surname': player.surname,
                    'chess_id': player.chess_id,
                    'date_of_birth': player.date_of_birth,
                    'score': player.score
                }
                json.dump(player_dict, json_file)
                json_file.write('\n')   

    @classmethod    
    def load_players_from_json(cls):
        all_players = []
        with open("data/player_list.json", "r") as json_file:
            for line in json_file:
                player_data = json.loads(line)
                player = cls(**player_data)
                all_players.append(player)


        print("\nListe des joueurs:\n")
        for player in all_players:
            print(f"{player}\n")
        
        return all_players

file_path = "/Users/guwoop/Documents/chess_tournament/data/player_list.json"