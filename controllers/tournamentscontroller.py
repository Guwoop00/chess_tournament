import json
import random
import math
from datetime import datetime
from views.player import PlayerView
from views.menu import MenuViews
from views.tournament import TournamentView
from controllers.playerscontroller import PlayerController
from models.player import Player
from models.round import Round
from models.tournament import Tournament

class TournamentController:
    def __init__(self):
        self.player_view = PlayerView()
        self.tournament_view = TournamentView()
        self.player_controller = PlayerController()
        self.menu_view = MenuViews()

    def launch_tournament(self):
        players_in_tournament = self.participating_players_list()
        tournament_data = self.create_new_tournament(players_in_tournament)
        total_rounds = int(tournament_data['total_rounds'])

        for current_round in range(1, total_rounds + 1):
            if current_round == 1:
                pairs = self.pair_players_randomly(players_in_tournament)
            else:
                pairs = self.pair_players_by_tournament_score(players_in_tournament, matches)
            matches = self.create_matches(pairs)
            round_name = Round(f"Round {current_round}/{total_rounds}", matches, end_time = None)
            print(round_name)
            for match in matches:
                choice = self.tournament_view.get_result_option(match)
                self.update_players_score(match, choice, players_in_tournament)
            round_name.end_time = self.tournament_view.finish_round()
            print(matches)       

    def pair_players_randomly(self, players_in_tournament):
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
        
    def pair_players_by_tournament_score(self, players_in_tournament, matches):
        number_of_matches_to_play = math.floor(len(players_in_tournament) / 2)
        players_available = players_in_tournament.copy()
        pairs = []
        for i in range(number_of_matches_to_play):
            player1 = players_available.pop(0)
            perfect_match = None
            for player2 in players_available:
                if not any((player1, player2) in match or (player2, player1) in match for match in matches):
                    perfect_match = players_available.pop(players_available.index(player2))
                    break
                 
            if perfect_match:
                pair = [player1, perfect_match]
                pairs.append(pair)
            else:
                player2 = players_available.pop(0)
                pair = [player1, player2]
                pairs.append(pair)
        return pairs

    def create_new_tournament(self, players_in_tournament):
        tournament_data = self.tournament_view.input_tournament_data(players_in_tournament)
        tournament_class = Tournament(
            tournament_data['name'],
            tournament_data['place'],
            datetime.now().strftime(f"à %H:%M:%S le %d-%m-%Y"),
            tournament_data['description'],
            players_in_tournament,
            tournament_data['total_rounds']
        )
        self.save_tournament_to_json(tournament_data)
        return tournament_data
                
    def participating_players_list(self):
        existing_players = self.player_controller.load_players_from_json(file_path="/Users/guwoop/Documents/chess_tournament/data/player_list.json")
        players_in_tournament = []

        while True:
            chess_id = self.player_view.chess_id_input()
            found_player = False

            for player_data in existing_players:
                if player_data['chess_id'] == chess_id:
                    new_player = Player(**player_data)

                    # Vérifie si le joueur est déjà dans la liste
                    if any(player.chess_id == new_player.chess_id for player in players_in_tournament):
                        self.tournament_view.added_already(new_player)
                        found_player = True
                    elif new_player not in players_in_tournament:
                        players_in_tournament.append(new_player)
                        self.tournament_view.added_to_tournament_input(new_player)
                        found_player = True
                    else:
                        found_player = False
                    break

            if not found_player:
                self.tournament_view.player_not_found_input()

            add_more = self.tournament_view.add_more_input()
            if add_more.lower() != "oui":
                break

        return players_in_tournament
    
    def save_tournament_to_json(self, tournament_data):
        with open("data/tournament_list.json", "a") as json_file:
            json.dump(tournament_data, json_file)
            json_file.write('\n')

    def load_tournaments_from_json(self, file_path):
        all_tournaments = []
        with open(file_path, "r") as json_file:
            for line in json_file:
                tournament_data = json.loads(line)              
                tournament = self.create_new_tournament(
                    tournament_data['name'],
                    tournament_data['place'],
                    tournament_data['start_date'],
                    tournament_data['end_date'],
                    tournament_data['description'],
                    tournament_data['players_list'],
                    tournament_data['total_rounds']                    
                )                
                all_tournaments.append(tournament)

    def create_matches(self, pairs):
        """
        return a match list
        """
        matches =[]
        for pair in pairs:      
            player1 = pair[0]
            player2 = pair[1]
            match = ( [f"{player1.name} {player1.surname}", player1.score],
                      [f"{player2.name} {player2.surname}", player2.score] )
            matches.append(match)
        return matches

    def update_players_score(self, match, choice, players_in_tournament):
        player1 = next(player for player in players_in_tournament if player.name + " " + player.surname == match[0][0])
        player2 = next(player for player in players_in_tournament if player.name + " " + player.surname == match[1][0])

        if choice == "1":
            match[0][1] += 1
            player1.update_score(1)
        elif choice == "N":
            match[0][1] += 0.5
            match[1][1] += 0.5
            player1.update_score(0.5)
            player2.update_score(0.5)
        elif choice == "2":
            match[1][1] += 1
            player2.update_score(1)
        elif choice == "Q":
            self.back_to_menu()
        else:
            self.menu_view.input_error()
            self.input_scores()

    @staticmethod
    def back_to_menu():
        from controllers.menu import MainController
        MainController.main_menu()