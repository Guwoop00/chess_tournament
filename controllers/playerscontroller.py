import json
from typing import Dict, List

from models.player import Player
from views.player import PlayerView


class PlayerController:
    def __init__(self):
        self.player_view = PlayerView()

    def create_new_player(self):
        """
        Create a new player and add them to the player database.

        Parameters:
        - name (str): The name of the new player.
        - surname (str): The surname of the new player.
        - chess_id (str): The official chess ID of the player.
        - date_of_birth (int): The official chess ID of the player.
        - score (int): The score of the player.

        Returns:
        - None

        This function creates a new player with the specified name, surname,
        chess_id, date_of_birth, score and adds them to the player database.
        If a player with the same name already exists,
        a warning message is logged and no new player is created.
        """
        while True:
            chess_id: str = self.player_view.chess_id_input()
            file_path: str = "data/player_list.json"
            existing_players: List[Dict[str, str]] = self.load_players_from_json(
                file_path
            )
            if self.player_exists(chess_id, existing_players):
                self.player_view.player_exists_output()
                return
            new_player_data: Dict[str, str] = self.player_view.input_player_data(
                chess_id
            )
            existing_players.append(new_player_data)
            self.save_players_to_json(existing_players, file_path)
            self.player_view.player_created()
            if not self.player_view.ask_to_add_another_player():
                break

    def player_exists(self, chess_id: str, players: List[Dict[str, str]]) -> bool:
        """
        Check if a player with the given chess ID exists
        in the list of players.

        Parameters:
        - chess_id (str): The chess ID to check.
        - players (list): A list of player dictionaries.

        Returns:
        - bool: True if a player with the given chess ID
        exists in the list of players, False otherwise.
        """
        return any(player["chess_id"] == chess_id for player in players)

    def load_players_from_json(self, file_path: str) -> List[Dict[str, str]]:
        """
        Load player data from a JSON file and
        return a list of player dictionaries.

        Parameters:
        - file_path (str): The path to the JSON file containing player data.

        Returns:
        - list: A list of player dictionaries loaded from the JSON file.

        If the JSON file cannot be decoded,
        an empty list is returned and an error message is displayed.
        """
        all_players: List[Dict[str, str]] = []
        try:
            with open(file_path, "r") as json_file:
                player_data_list: List[Dict[str, str]] = json.load(json_file)
                for player_data in player_data_list:
                    player = Player(**player_data)
                    all_players.append(player.to_json())
        except json.decoder.JSONDecodeError:
            self.player_view.empty_json_print()
        return all_players

    def save_players_to_json(
        self, all_players: List[Dict[str, str]], file_path: str
    ) -> None:
        """
        Save a list of player dictionaries to a JSON file.

        Parameters:
        - all_players (list): A list of player dictionaries to be saved.
        - file_path (str): The file path where the JSON file will be saved.

        Returns:
        - None

        This function saves the list of player dictionaries provided in
        'all_players' to the specified
        JSON file located at 'file_path'. The data is formatted with
        an indentation level of 4 spaces
        for readability.
        """
        with open(file_path, "w") as json_file:
            json.dump(all_players, json_file, indent=4)
