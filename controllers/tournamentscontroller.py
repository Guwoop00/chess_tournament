import json
import math
import random
from typing import Any, Dict, List, Tuple

from controllers.playerscontroller import PlayerController
from models.round import Round
from models.tournament import Tournament
from models.match import Match
from views.menu import MenuViews
from views.player import PlayerView
from views.tournament import TournamentView


class TournamentController:

    def __init__(self):
        """
        Initializes the TournamentController.
        """
        self.player_view = PlayerView()
        self.tournament_view = TournamentView()
        self.player_controller = PlayerController()
        self.menu_view = MenuViews()

    def launch_tournament(self) -> None:
        """
        Orchestrates the process of launching a new tournament.
        """
        players_in_tournament: List[Dict[str, Any]] = self.participating_players_list()
        new_tournament_data: Dict[str, Any] = self.create_new_tournament(
            players_in_tournament
        )
        self.run_tournament(new_tournament_data, players_in_tournament)

    def run_tournament(
        self,
        new_tournament_data: Dict[str, Any],
        players_in_tournament: List[Dict[str, Any]],
    ) -> None:
        """
        Runs a tournament with the given data and players.

        Args:
            new_tournament_data (dict): The data of the new tournament.
            players_in_tournament (list): The list of participating players.
        """
        total_rounds: int = int(new_tournament_data["total_rounds"])
        self.verify_if_rounds_exist(new_tournament_data)
        initial_round: int = self.verify_if_current_round_exist(new_tournament_data)
        pairs_history: List[Tuple[str, str]] = self.verify_if_pairs_history_exist(
            new_tournament_data
        )
        for current_round in range(initial_round, total_rounds + 1):
            round_name, matches = self.run_rounds(
                new_tournament_data,
                current_round,
                total_rounds,
                players_in_tournament,
                pairs_history,
            )
            self.save_rounds_to_json()
            self.ask_for_match_result(matches, players_in_tournament)
            all_tournaments = self.load_tournament_from_json(
                "data/tournament_list.json"
            )
            for match in matches:
                new_tournament_json = self.update_tournament_data(
                    new_tournament_data,
                    current_round,
                    total_rounds,
                    round_name,
                    match,
                    all_tournaments,
                    pairs_history,
                )
        resume = self.tournament_view.display_tournament_summary(new_tournament_json)
        self.tournament_view.display_resume(resume)

    def verify_if_rounds_exist(
        self, new_tournament_data: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """
        Verifies if rounds exist in the tournament data.

        Args:
            new_tournament_data (dict): The data of the new tournament.

        Returns:
            list: The list of rounds if founded, an empty list otherwise.
        """
        if "rounds" not in new_tournament_data:
            new_tournament_data["rounds"] = []
        return new_tournament_data["rounds"]

    def verify_if_current_round_exist(self, new_tournament_data: Dict[str, Any]) -> int:
        """
        Verifies if the current round exists in the tournament data.

        Args:
            new_tournament_data (dict): The data of the new tournament.

        Returns:
            int: The initial round number.
        """
        if "current_round" in new_tournament_data:
            initial_round = new_tournament_data["current_round"] + 1
        else:
            initial_round = 1
        return initial_round

    def verify_if_pairs_history_exist(
        self, new_tournament_data: Dict[str, Any]
    ) -> List[Tuple[str, str]]:
        """
        Verifies if the pairs history exists in the tournament data.

        Args:
            new_tournament_data (dict): The data of the new tournament.

        Returns:
            A list of pairs history.
        """
        if "pairs_history" in new_tournament_data:
            pairs_history = new_tournament_data["pairs_history"]
        else:
            pairs_history = []
        return pairs_history

    def run_rounds(
        self,
        new_tournament_data: Dict[str, Any],
        current_round: int,
        total_rounds: int,
        players_in_tournament: List[Dict[str, Any]],
        pairs_history: List[Tuple[str, str]],
    ) -> Tuple[Round, List[Tuple[Dict[str, Any], Dict[str, Any]]]]:
        """
        Runs rounds for the tournament.

        Args:
            new_tournament_data (dict): The data of the new tournament.
            current_round (int): The current round number.
            total_rounds (int): The total number of rounds in the tournament.
            players_in_tournament (list): The list of participating players.

        Returns:
            tuple: A tuple containing the round name and matches.
        """
        new_tournament_data["current_round"] = current_round
        if current_round == 1:
            pairs = self.pair_players_randomly(players_in_tournament, pairs_history)
        else:
            pairs = self.pair_by_tournament_score(players_in_tournament, pairs_history)
        matches = self.create_matches(pairs)
        round_name = Round(f"Round {current_round}/{total_rounds}", matches)
        self.tournament_view.display_round_name(round_name)
        return round_name, matches

    def save_rounds_to_json(self) -> None:
        """
        Saves the rounds to a JSON file.
        """
        all_tournaments = self.load_tournament_from_json("data/tournament_list.json")
        self.save_tournament_to_json(all_tournaments, "data/tournament_list.json")

    def ask_for_match_result(
        self,
        matches: List[Tuple[Dict[str, Any], Dict[str, Any]]], players_in_tournament
    ) -> None:
        """
        Prompt for match results and update players' scores.

        Args:
            matches (list): List of matches to evaluate.
            players_in_tournament (list):
            List of players participating in the tournament.
        """
        for match in matches:
            match_result_choice = self.tournament_view.get_result_option(match)
            self.update_players_score(match, match_result_choice, players_in_tournament)

    def update_tournament_data(
        self,
        new_tournament_data: Dict[str, Any],
        current_round: int,
        total_rounds: int,
        round_name: Round,
        matches: List[Tuple[Dict[str, Any], Dict[str, Any]]],
        all_tournaments: List[Dict[str, Any]],
        pairs_history: List[Tuple[str, str]],
    ) -> Dict[str, Any]:
        """
        Update tournament data after a round.

        Args:
            new_tournament_data (dict): Data of the new tournament.
            current_round (int): Current round number.
            total_rounds (int): Total number of rounds in the tournament.
            round_name (Round): Object representing the current round.
            matches (list): List of matches in the round.
            all_tournaments (list): List of all tournaments.
        """
        round_name.end_time = self.tournament_view.finish_round()
        if current_round == total_rounds:
            new_tournament_data["end_date"] = round_name.end_time
        self.tournament_view.display_matches(matches)
        round_name.matches = matches.to_json()
        new_round_data = round_name.to_json()
        new_tournament_data["rounds"].append(new_round_data)
        new_tournament_data["pairs_history"] = pairs_history
        new_tournament_json = Tournament(**new_tournament_data).to_json()
        for i, tournament in enumerate(all_tournaments):
            if tournament["name"] == new_tournament_data["name"]:
                all_tournaments[i] = new_tournament_json
                break
        else:
            all_tournaments.append(new_tournament_json)
        self.save_tournament_to_json(all_tournaments, "data/tournament_list.json")
        return new_tournament_json

    def pair_players_randomly(
        self,
        players_in_tournament: List[Dict[str, Any]],
        pairs_history: List[Tuple[str, str]],
    ) -> List[Tuple[Dict[str, Any], Dict[str, Any]]]:
        """
        Form pairs of players randomly.

        Args:
            players_in_tournament (list):
            List of players participating in the tournament.

        Returns:
            list: List of player pairs.
        """
        number_of_matches_to_play = math.floor(len(players_in_tournament) / 2)
        players_available = players_in_tournament.copy()
        pairs = []
        random.shuffle(players_available)
        for _ in range(number_of_matches_to_play):
            player1 = players_available.pop()
            player2 = players_available.pop()
            pair = (player1, player2)
            pair_history = (player1["chess_id"], player2["chess_id"])
            pairs.append(pair)
            pairs_history.append(pair_history)
        return pairs

    def pair_by_tournament_score(
        self,
        players_in_tournament: List[Dict[str, Any]],
        pairs_history: List[Tuple[str, str]],
    ) -> List[Tuple[Dict[str, Any], Dict[str, Any]]]:
        """
        Pair players for a tournament based on their scores.

         Args:
             players_in_tournament (list):
             A list of dictionaries representing players
                 in the tournament.
             Each dictionary should contain at least a "score"
                 key representing the player's score.

         Returns:
             list: A list of pairs, where each pair
             consists of two players. The pairs
                 are determined based on the players'
                 scores, with higher-scoring players
                 being paired together where possible.

         Note:
             The function sorts players by their scores
             in descending order before
             pairing them. If there are multiple pairs
             that can be formed with the
             same two players, the function selects the
             pair that has not been formed
             previously.

        """
        pairs = []
        number_of_matches_to_play = math.floor(len(players_in_tournament) / 2)
        players_available = players_in_tournament.copy()
        players_available = sorted(
            players_available, key=lambda player: player["score"], reverse=True
        )
        for _ in range(number_of_matches_to_play):
            player1 = players_available.pop(0)
            found_player2 = False
            for player2 in players_available:
                if (player1["chess_id"], player2["chess_id"]) not in pairs_history and (
                    player2["chess_id"],
                    player1["chess_id"],
                ) not in pairs_history:
                    players_available.remove(player2)
                    pair = [player1, player2]
                    pairs.append(pair)
                    pairs_history.append((player1["chess_id"], player2["chess_id"]))
                    found_player2 = True
                    break
            if found_player2 is False:
                player2 = players_available.pop(0)
                pair = [player1, player2]
                pairs.append(pair)
        return pairs

    def create_new_tournament(
        self, players_in_tournament: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Create a new tournament.

        Args:
            players_in_tournament (list):
            List of players participating in the tournament.

        Returns:
            dict: Data of the new tournament.
        """
        file_path: str = "data/tournament_list.json"
        all_tournaments: List[Dict[str, Any]] = self.load_tournament_from_json(
            file_path
        )
        new_tournament_data: Dict[str, Any] = (
            self.tournament_view.input_tournament_data(players_in_tournament)
        )
        all_tournaments.append(new_tournament_data)
        self.save_tournament_to_json(all_tournaments, file_path)
        return new_tournament_data

    def participating_players_list(self) -> List[Dict[str, Any]]:
        """
        Form the list of players participating in the tournament.

        Returns:
            list: List of players participating in the tournament.
        """
        existing_players: List[Dict[str, Any]] = (
            self.player_controller.load_players_from_json("data/player_list.json")
        )
        players_in_tournament: List[Dict[str, Any]] = []
        while True:
            chess_id = self.player_view.chess_id_input()
            found_player = False
            for player_data in existing_players:
                if player_data["chess_id"] == chess_id:
                    if any(
                        player["chess_id"] == player_data["chess_id"]
                        for player in players_in_tournament
                    ):
                        self.tournament_view.added_already(player_data)
                        found_player = True
                    elif player_data not in players_in_tournament:
                        players_in_tournament.append(player_data)
                        self.tournament_view.added_to_tournament_input(player_data)
                        found_player = True
                    else:
                        found_player = False
                    break
            if not found_player:
                self.tournament_view.player_not_found_input()
            add_more: str = self.tournament_view.add_more_input()
            if add_more != "":
                if self.verify_pair_players(players_in_tournament):
                    break
                else:
                    self.tournament_view.must_be_pair()

        return players_in_tournament

    def save_tournament_to_json(
        self, all_tournaments: List[Dict[str, Any]], file_path: str
    ) -> None:
        """
        Save tournaments to a JSON file.

        Args:
            all_tournaments (list): List of tournaments.
            file_path (str): Path to the JSON file for saving.
        """
        with open(file_path, "w") as json_file:
            json.dump(all_tournaments, json_file, indent=4)

    def load_most_recent_tournament(self, file_path: str) -> None:
        """
        Load the most recent ongoing tournament.

        Args:
            file_path (str): Path to the JSON file containing tournaments.
        """
        all_tournaments: List[Dict[str, Any]] = self.load_tournament_from_json(
            file_path
        )
        sorted_tournaments: List[Dict[str, Any]] = sorted(
            all_tournaments,
            key=lambda tournament: tournament["start_date"],
            reverse=True,
        )
        if not sorted_tournaments:
            self.tournament_view.no_unfinished_tournament()
        else:
            most_recent_tournament: Dict[str, Any] = sorted_tournaments[0]
            if most_recent_tournament["end_date"] is None:
                new_tournament_data: Dict[str, Any] = Tournament(
                    **most_recent_tournament
                ).to_json()
                players_in_tournament: List[Dict[str, Any]] = new_tournament_data[
                    "players_in_tournament"
                ]
                self.run_tournament(new_tournament_data, players_in_tournament)
            else:
                self.tournament_view.no_unfinished_tournament()

    def load_tournament_from_json(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Load all tournaments from a JSON file.

        Args:
            file_path (str): Path to the JSON file containing tournaments.

        Returns:
            list: List of all tournaments.
        """
        all_tournaments: List[Dict[str, Any]] = []
        try:
            with open(file_path, "r") as json_file:
                tournament_data_list: List[Dict[str, Any]] = json.load(json_file)
                for tournament_data in tournament_data_list:
                    tournament = Tournament(**tournament_data)
                    all_tournaments.append(tournament.to_json())
        except json.decoder.JSONDecodeError:
            self.player_view.empty_json_print()
        return all_tournaments

    def create_matches(
        self, pairs: List[Tuple[Dict[str, Any], Dict[str, Any]]]
    ) -> List[Tuple[List[str], List[int]]]:
        """
        Create matches from pairs of players.

        Args:
            pairs (list): List of player pairs.

        Returns:
            list: List of matches.
        """
        matches = []
        for pair in pairs:
            player1 = (pair[0]["name"], pair[0]["surname"], pair[0]["score"])
            player2 = (pair[1]["name"], pair[1]["surname"], pair[1]["score"])
            match = Match(player1, pair[0]["score"], player2, pair[1]["score"])
            matches.append(match)
        return matches

    def update_players_score(
        self,
        match: Match,
        match_result_choice: str,
        players_in_tournament: List[Dict[str, Any]]
    ):
        """
        Update players' scores based on match results.

        Args:
            match (Match): Match details.
            match_result_choice (str): Player's choice for match result.
            players_in_tournament (list): List of players participating in the tournament.
        """
        player1 = next(
            player
            for player in players_in_tournament
            if player["name"] + " " + player["surname"] == match.players[0][0][0] + " " + match.players[0][0][1]
        )
        player2 = next(
            player
            for player in players_in_tournament
            if player["name"] + " " + player["surname"] == match.players[1][0][0] + " " + match.players[1][0][1]
        )
        if match_result_choice == "1":
            player1["score"] += 1
        elif match_result_choice == "N":
            player1["score"] += 0.5
            player2["score"] += 0.5
        elif match_result_choice == "2":
            player2["score"] += 1
        elif match_result_choice == "Q":
            exit()
        else:
            self.menu_view.input_error()

    def verify_pair_players(self, players_in_tournament: List[Dict[str, Any]]) -> bool:
        """
        Verify if the number of players is even.

        Args:
            players_in_tournament (list):
            List of players participating in the tournament.

        Returns:
            bool: True if the number of players is even, False otherwise.
        """
        return len(players_in_tournament) % 2 == 0
