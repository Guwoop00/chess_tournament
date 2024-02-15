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
from models.match import Match
from models.tournament import Tournament
from random import randrange

class TournamentController:
    def __init__(self):
        self.player_view = PlayerView()
        self.tournament_view = TournamentView()
        self.player_controller = PlayerController()

    def start_tournament(self):
        players_in_tournament = self.participating_players_list()
        tournament_data = self.create_new_tournament(players_in_tournament)
        total_rounds = int(tournament_data['total_rounds'])

        for current_round in range(1, total_rounds + 1):
            matchs = self.pairing_players(players_in_tournament, current_round)
            round_name = Round(f"Round {current_round}/{total_rounds}", matchs)
            print(round_name)


    def pairing_players(self, players_in_tournament, current_round):
        matchs_possible = math.floor(len(players_in_tournament) / 2)
        if current_round == 1:
            players_in_tournament.sort(key=lambda x: x.score, reverse=True)
            matchs = []
            for i in range(matchs_possible):
                player1 = players_in_tournament.pop(randrange(len(players_in_tournament)))
                player2 = players_in_tournament.pop(randrange(len(players_in_tournament)))
                match = self.create_matchs(player1, player2)
                matchs.append(match)
            return matchs

    def create_new_tournament(self, players_in_tournament):
        tournament_data = self.tournament_view.input_tournament_data(players_in_tournament)
        tournament_class = Tournament(
            tournament_data['name'],
            tournament_data['place'],
            tournament_data['start_date'],
            tournament_data['end_date'],
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
    
    def save_tournament_to_json(self, tournament_dict):
        with open("data/tournament_list.json", "a") as json_file:
            json.dump(tournament_dict, json_file)
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

    def create_matchs(self, player1, player2):
        """
        return a match list
        """
        match = (
            f"{player1.name}, {player1.surname}",
            player1.score,
            f"{player2.name}, {player2.surname}",
            player2.score
        )
        return match
