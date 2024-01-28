import json

class Player:
    def __init__(self, name, surname, chess_id, date_of_birth, score=0):
        self.name = name
        self.surname = surname
        self.chess_id = chess_id
        self.date_of_birth = date_of_birth
        self.score = score

    def __str__(self):
        return f"{self.name} {self.surname}\n{self.chess_id}\n{self.date_of_birth}"

    @classmethod
    def save_players(cls, players):
        with open("data/player_list.json", "w") as json_file:
            for player in players:
                player_data = {
                    "name": player.name,
                    "surname": player.surname,
                    "chess_id": player.chess_id,
                    "date_of_birth": player.date_of_birth,
                    "score": player.score
                }
                json.dump(player_data, json_file)
                json_file.write('\n')   
    
    @classmethod
    def load_players(cls):
        player_list = []
        with open("data/player_list.json", "r") as json_file:
            for line in json_file:
                player_data = json.loads(line)
                player = cls(player_data["name"], player_data["surname"], player_data["chess_id"], player_data["date_of_birth"], player_data["score"])
                player_list.append(player)
        return player_list
        
    @classmethod    
    def display_all_players(cls, file_path):
        display_list =[]
        with open(file_path, "r") as json_file:
            for line in json_file:
                player_data = json.loads(line) #Conversion du JSON
                player = cls(**player_data) #..
                display_list.append(player)

        print("\nListe des joueurs:\n")
        for player in display_list:
            print(f"{player}\n")

file_path = "/Users/guwoop/Documents/chess_tournament/data/player_list.json"

if __name__ == "__main__":
    Player.display_all_players(file_path)