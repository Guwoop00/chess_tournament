import json
from views.player import PlayerView
from views.tournament import TournamentView
from controllers.playerscontroller import PlayerController


class TournamentController:
    def __init__(self):
        self.player_view = PlayerView()
        self.tournament_view = TournamentView()
        self.player_controller = PlayerController()

    def create_new_tournament(self):
        players_in_tournament = self.participating_players_list()
        tournament_dict = self.tournament_view.input_tournament_data(players_in_tournament)
        self.save_tournament_to_json(tournament_dict)
        
    def participating_players_list(self):
        existing_players = self.player_controller.load_players_from_json(file_path = "/Users/guwoop/Documents/chess_tournament/data/player_list.json")
        players_in_tournament = []
        while True:
            chess_id = self.player_view.chess_id_input()
            found_player = False
            for player in existing_players:
                if player.chess_id == chess_id:
                    players_in_tournament.append(player)
                    self.tournament_view.added_to_tournament_input(player)
                    found_player = True
                    break  
            if not found_player:
                self.tournament_view.player_not_found_input()
            else:
                add_more = self.tournament_view.add_more_input()
                if add_more.lower() != "oui":
                    break

        return players_in_tournament
    
    def save_tournament_to_json(self, tournament_data):
        with open("data/tournament_list.json", "a") as json_file:
            json.dump(tournament_data, json_file)
            json_file.write('\n')


    def load_tournaments_from_json(cls, file_path):
        all_tournaments = []
        with open(file_path, "r") as json_file:
            for line in json_file:
                tournament_data = json.loads(line)
                
                tournament_controller = cls()
                tournament_controller.save_tournament_to_json(tournament_data)
                
                tournament = tournament_controller.create_new_tournament(
                    tournament_data['name'],
                    tournament_data['place'],
                    tournament_data['start_date'],
                    tournament_data['end_date'],
                    tournament_data['description'],
                    tournament_data['players_list']
                )
                
                all_tournaments.append(tournament)
