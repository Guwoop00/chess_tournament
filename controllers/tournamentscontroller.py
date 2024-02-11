import json
import random
from datetime import datetime
from views.player import PlayerView
from views.menu import MenuViews
from views.tournament import TournamentView
from controllers.playerscontroller import PlayerController
from models.player import Player
from models.round import Round
from models.tournament import Tournament
from random import randrange
import math

class TournamentController:
    def __init__(self):
        self.player_view = PlayerView()
        self.tournament_view = TournamentView()
        self.player_controller = PlayerController()
        self.menu_view = MenuViews()
        self.timer = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def start_tournament(self, players_in_tournament):
        total_rounds = Tournament.total_rounds
        for i in range (1, total_rounds + 1, 1):
            # Creer l'instance de round et l'afficher
            pairs = self.pairing_players(players_in_tournament)
            self.create_matchs(pairs)
            print(pairs)

    def pairing_players(self, players_in_tournament):
        matchs_possible = math.floor(len(players_in_tournament)/2)
        players_list = players_in_tournament
        players_list.sort(key=lambda x: x.score, reverse=True)
        pairs = []
        if players_list[0].score == 0:
            for i in range(matchs_possible):
                player1 = players_list.pop(randrange(len(players_list)))
                player2 = players_list.pop(randrange(len(players_list)))
                pair = (player1, player2)
                pairs.append(pair)
                print(player1, player2)
            print(pairs)
            return pairs


    def create_new_tournament(self,players_in_tournament):
        tournament_dict = self.tournament_view.input_tournament_data(players_in_tournament)
        self.save_tournament_to_json(tournament_dict)
                
    def participating_players_list(self):
        existing_players = self.player_controller.load_players_from_json(file_path="/Users/guwoop/Documents/chess_tournament/data/player_list.json")
        players_in_tournament = []
        while True:
            chess_id = self.player_view.chess_id_input()
            found_player = False
            for player_data in existing_players:
                if player_data['chess_id'] == chess_id:
                    player = Player(**player_data)
                    players_in_tournament.append(player)
                    self.tournament_view.added_to_tournament_input(player)
                    found_player = True
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
                self.save_tournament_to_json(tournament_data)                
                tournament = self.create_new_tournament(
                    tournament_data['name'],
                    tournament_data['place'],
                    tournament_data['start_date'],
                    tournament_data['end_date'],
                    tournament_data['description'],
                    tournament_data['players_list']
                )
                
                all_tournaments.append(tournament)

    def sort_players_randomly(players_in_tournament):
        random.shuffle(players_in_tournament)
        for i, player in enumerate(players_in_tournament, start=1):
            globals()[f"player{i}"] = player

    def create_matchs(self, pairing_players):
        """
        return a match list
        """
        matchs = []
        for pair in pairing_players:
            player1 = pair[0]
            player2 = pair[1]
            
            match = (
                f"{player1.name}, {player1.surname}",
                player1.score,
                f"{player2.name}, {player2.surname}",
                player2.score
            )
            print(match)
            matchs.append(match)
        print(matchs)
        return matchs
