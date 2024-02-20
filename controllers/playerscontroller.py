import json
from views.player import PlayerView
from models.player import Player


class PlayerController:
    def __init__(self):
        self.player_view = PlayerView()

    def create_new_player(self):
        while True:  # Boucle de création de joueur
            chess_id = self.player_view.chess_id_input()
            file_path = "/Users/guwoop/Documents/chess_tournament"
            "/data/player_list.json"

            # Liste de tous les joueurs
            existing_players = self.load_players_from_json(file_path)

            # Recherche si le joueur existe déjà avec son chess_id
            if self.player_exists(chess_id, existing_players):
                self.player_view.player_exists_output()
                return
            # Récolte des datas d'un nouveau joueur
            new_player_data = self.player_view.input_player_data(chess_id)
            existing_players.append(new_player_data)

            # Enregistrement des datas du joueur
            self.save_players_to_json(existing_players, file_path)
            self.player_view.player_created()

            # Boucle ou fin de création de joueur
            if not self.player_view.ask_to_add_another_player():
                break

    # Pour chaque joueur dans la liste, vérifie si le chess_id existe déjà

    def player_exists(self, chess_id, players):
        return any(player["chess_id"] == chess_id for player in players)

    # Charge les joueurs depuis le fichier JSON
    def load_players_from_json(self, file_path):
        all_players = []
        try:
            with open(file_path, "r") as json_file:
                player_data_list = json.load(json_file)
                for player_data in player_data_list:
                    # Création d'un objet Player avec les datas du fichier JSON
                    player = Player(**player_data)
                    all_players.append(player.to_json())
        # Exception si le fichier JSON est vide
        except json.decoder.JSONDecodeError:
            self.player_view.empty_json_print()
        return all_players

    # Enregistre les joueurs dans le fichier JSON
    def save_players_to_json(self, all_players, file_path):
        with open(file_path, "w") as json_file:
            json.dump(all_players, json_file, indent=4)


if __name__ == "__main__":
    player_controller = PlayerController()
    player_controller.create_new_player()
