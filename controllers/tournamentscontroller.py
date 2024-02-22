import json
import random
import math
from views.player import PlayerView
from views.menu import MenuViews
from views.tournament import TournamentView
from controllers.playerscontroller import PlayerController
from models.round import Round
from models.tournament import Tournament


class TournamentController:

    def __init__(self):
        """Initializes the TournamentController."""
        self.player_view = PlayerView()
        self.tournament_view = TournamentView()
        self.player_controller = PlayerController()
        self.menu_view = MenuViews()

    def launch_tournament(self):
        """
        This function orchestrates the process of launching a new tournament.
        It retrieves the list of participating players
        using 'participating_players_list',
        then runs the tournament using 'run_tournament'
        with the newly created tournament data.
        """
        players_in_tournament = self.participating_players_list()
        new_tournament_data = self.create_new_tournament(players_in_tournament)
        self.run_tournament(new_tournament_data, players_in_tournament)

    def run_tournament(self, new_tournament_data, players_in_tournament):
        """
        Runs a tournament with the given data and players.

        Args:
            new_tournament_data (dict): The data of the new tournament.
            players_in_tournament (list): The list of participating players.
        """
        total_rounds = int(new_tournament_data['total_rounds'])
        self.verify_if_rounds_exist(new_tournament_data)
        initial_round = self.verify_if_current_round_exist(new_tournament_data)
        for current_round in range(initial_round, total_rounds + 1):
            round_name, matches = self.run_rounds(new_tournament_data,
                                                  current_round, total_rounds,
                                                  players_in_tournament)
            self.save_rounds_to_json()
            self.ask_for_match_result(matches, players_in_tournament)
            all_tournaments = self.load_tournament_from_json(
                'data/tournament_list.json')
            self.update_tournament_data(new_tournament_data, current_round,
                                        total_rounds, round_name, matches,
                                        all_tournaments)

    def verify_if_rounds_exist(self, new_tournament_data):
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

    def verify_if_current_round_exist(self, new_tournament_data):
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

    def run_rounds(self, new_tournament_data, current_round,
                   total_rounds, players_in_tournament):
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
            pairs = self.pair_players_randomly(players_in_tournament)
        else:
            pairs = self.pair_by_tournament_score(players_in_tournament)
        matches = self.create_matches(pairs)
        round_name = Round(f"Round {current_round}/{total_rounds}",
                           f"{matches}")
        print(round_name)
        return round_name, matches

    def save_rounds_to_json(self):
        """
        Saves the rounds to a JSON file.
        """
        all_tournaments = self.load_tournament_from_json(
         'data/tournament_list.json')
        self.save_tournament_to_json(all_tournaments,
                                     'data/tournament_list.json')

    def ask_for_match_result(self, matches, players_in_tournament):
        """
        Prompt for match results and update players' scores.

        Args:
            matches (list): List of matches to evaluate.
            players_in_tournament (list):
            List of players participating in the tournament.
        """
        for match in matches:
            choice = self.tournament_view.get_result_option(match)
            self.update_players_score(match, choice, players_in_tournament)

    def update_tournament_data(self, new_tournament_data, current_round,
                               total_rounds, round_name,
                               matches, all_tournaments):
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
        print(matches)
        new_tournament_data["rounds"].append(round_name.to_json())
        new_tournament_json = Tournament(**new_tournament_data).to_json()
        for i, tournament in enumerate(all_tournaments):
            if tournament['name'] == new_tournament_data['name']:
                all_tournaments[i] = new_tournament_json
                break
        else:
            all_tournaments.append(new_tournament_json)
        self.save_tournament_to_json(all_tournaments,
                                     'data/tournament_list.json')

    def pair_players_randomly(self, players_in_tournament):
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
        for i in range(number_of_matches_to_play):
            player1 = players_available.pop()
            player2 = players_available.pop()
            pair = (player1, player2)
            pairs.append(pair)
        return pairs

    def pair_by_tournament_score(self, players_in_tournament):
        """
        Form pairs of players based on their scores and previous opponents.

        Args:
            players_in_tournament (list):
            List of players participating in the tournament.

        Returns:
            list: List of player pairs.
        """
        number_of_matches_to_play = math.floor(len(players_in_tournament) / 2)
        players_available = players_in_tournament.copy()
        players_available = sorted(players_available,
                                   key=lambda player: player["score"],
                                   reverse=True)
        pairs = []
        for i in range(number_of_matches_to_play):
            player1 = players_available.pop(0)
            perfect_match = None
            for player2 in players_available:
                if not any((player1, player2) in pair or (player2, player1)
                           in pair for pair in pairs):
                    perfect_match = players_available.pop(
                        players_available.index(player2))
                    break
            if perfect_match:
                pair = [player1, perfect_match]
            else:
                player2 = players_available.pop(0)
                pair = [player1, player2]
            pairs.append(pair)
        return pairs

    def create_new_tournament(self, players_in_tournament):
        """
        Create a new tournament.

        Args:
            players_in_tournament (list):
            List of players participating in the tournament.

        Returns:
            dict: Data of the new tournament.
        """
        file_path = "data/tournament_list.json"
        all_tournaments = self.load_tournament_from_json(file_path)
        new_tournament_data = self.tournament_view.input_tournament_data(
            players_in_tournament)
        all_tournaments.append(new_tournament_data)
        self.save_tournament_to_json(all_tournaments, file_path)
        return new_tournament_data

    def participating_players_list(self):
        """
        Form the list of players participating in the tournament.

        Returns:
            list: List of players participating in the tournament.
        """
        existing_players = self.player_controller.load_players_from_json(
            "data/player_list.json")
        players_in_tournament = []
        while True:
            chess_id = self.player_view.chess_id_input()
            found_player = False
            for player_data in existing_players:
                if player_data['chess_id'] == chess_id:
                    if any(player['chess_id'] == player_data["chess_id"]
                           for player in players_in_tournament):
                        self.tournament_view.added_already(player_data)
                        found_player = True
                    elif player_data not in players_in_tournament:
                        players_in_tournament.append(player_data)
                        self.tournament_view.added_to_tournament_input(
                            player_data)
                        found_player = True
                    else:
                        found_player = False
                    break
            if not found_player:
                self.tournament_view.player_not_found_input()
            add_more = self.tournament_view.add_more_input()
            if add_more.lower() != "oui":
                if self.verify_pair_players(players_in_tournament):
                    break
                else:
                    print("Le nombre de joueur doit etre pair. "
                          "Ajoutez un autre joueur.")
        return players_in_tournament

    def save_tournament_to_json(self, all_tournaments, file_path):
        """
        Save tournaments to a JSON file.

        Args:
            all_tournaments (list): List of tournaments.
            file_path (str): Path to the JSON file for saving.
        """
        with open(file_path, "w") as json_file:
            json.dump(all_tournaments, json_file, indent=4)

    def load_most_recent_tournament(self, file_path):
        """
        Load the most recent ongoing tournament.

        Args:
            file_path (str): Path to the JSON file containing tournaments.
        """
        all_tournaments = self.load_tournament_from_json(file_path)
        sorted_tournaments = sorted(all_tournaments,
                                    key=lambda tournament:
                                    tournament['start_date'], reverse=True)
        if not sorted_tournaments:
            self.tournament_view.no_unfinished_tournament()
        else:
            most_recent_tournament = sorted_tournaments[0]
            if most_recent_tournament['end_date'] is None:
                new_tournament_data = Tournament(
                    **most_recent_tournament).to_json()
                players_in_tournament = new_tournament_data[
                    'players_in_tournament']
                print(new_tournament_data)
                self.run_tournament(new_tournament_data, players_in_tournament)
            else:
                self.tournament_view.no_unfinished_tournament()

    def load_tournament_from_json(self, file_path):
        """
        Load all tournaments from a JSON file.

        Args:
            file_path (str): Path to the JSON file containing tournaments.

        Returns:
            list: List of all tournaments.
        """
        all_tournaments = []
        try:
            with open(file_path, "r") as json_file:
                tournament_data_list = json.load(json_file)
                for tournament_data in tournament_data_list:
                    tournament = Tournament(**tournament_data)
                    all_tournaments.append(tournament.to_json())
        except json.decoder.JSONDecodeError:
            self.player_view.empty_json_print()
        return all_tournaments

    def create_matches(self, pairs):
        """
        Create matches from pairs of players.

        Args:
            pairs (list): List of player pairs.

        Returns:
            list: List of matches.
        """
        matches = []
        for pair in pairs:
            player1 = pair[0]
            player2 = pair[1]
            match = ([f"{player1['name']} {player1['surname']}",
                      player1['score']], [f"{player2['name']} "
                                          f"{player2['surname']}",
                                          player2['score']])
            matches.append(match)
        return matches

    def update_players_score(self, match, choice, players_in_tournament):
        """
       Update players' scores based on match results.

        Args:
            match (list): Match details.
            choice (str): Player's choice for match result.
            players_in_tournament (list):
            List of players participating in the tournament.
        """
        player1 = next(player for player in players_in_tournament if
                       player['name'] + " " + player['surname'] == match[0][0])
        player2 = next(player for player in players_in_tournament if
                       player['name'] + " " + player['surname'] == match[1][0])
        if choice == "1":
            match[0][1] += 1
            player1['score'] += 1
        elif choice == "N":
            match[0][1] += 0.5
            match[1][1] += 0.5
            player1['score'] += 0.5
            player2['score'] += 0.5
        elif choice == "2":
            match[1][1] += 1
            player2['score'] += 1
        elif choice == "Q":
            exit()
        else:
            self.menu_view.input_error()

    def verify_pair_players(self, players_in_tournament):
        """
        Verify if the number of players is even.

        Args:
            players_in_tournament (list):
            List of players participating in the tournament.

        Returns:
            bool: True if the number of players is even, False otherwise.
        """
        return len(players_in_tournament) % 2 == 0
