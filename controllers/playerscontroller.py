import json
import os
from views.player import PlayerView
from models.player import Player

class PlayerController:
    def __init__(self):
        self.player_view = PlayerView()
    
    def create_new_player(self):
        chess_id = self.player_view.chess_id_input()
        file_path = "/Users/guwoop/Documents/chess_tournament/data/player_list.json"
        existing_players = self.load_players_from_json(file_path)
        
        if self.player_exists(chess_id, existing_players):
            self.player_view.player_exists_output()
            return
        
        new_player_data = self.player_view.input_player_data(chess_id)
        existing_players.append(new_player_data)

        self.save_players_to_json(existing_players, file_path)
        self.player_view.player_created()

    def player_exists(self, chess_id, players):
        for player in players:
            if player["chess_id"] == chess_id:
                return True
        return False
       
    def load_players_from_json(self, file_path):
        all_players = []
        try:
            with open(file_path, "r") as json_file:
                player_data_list = json.load(json_file)
                for player_data in player_data_list:
                    player = Player(**player_data)
                    all_players.append(player.to_json())
        except json.decoder.JSONDecodeError:
            # Le fichier est vide ou contient un JSON invalide
            print("Le fichier JSON est vide ou invalide.")
        return all_players

    def save_players_to_json(self, all_players, file_path):
        with open(file_path, "w") as json_file:
            json.dump(all_players, json_file)


if __name__ == "__main__":
    player_controller = PlayerController()
    player_controller.create_new_player()
