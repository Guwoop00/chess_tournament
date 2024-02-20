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
        self.player_view = PlayerView()
        self.tournament_view = TournamentView()
        self.player_controller = PlayerController()
        self.menu_view = MenuViews()

    def launch_tournament(self):
        players_in_tournament = self.participating_players_list()
        new_tournament_data = self.create_new_tournament(players_in_tournament)
        total_rounds = int(new_tournament_data['total_rounds'])
        self.run_tournament(
            new_tournament_data, players_in_tournament, total_rounds
        )

    def run_tournament(
            self, new_tournament_data, players_in_tournament, total_rounds
            ):
        new_tournament_data["rounds"] = []

        # Boucle de création des rounds
        for current_round in range(1, total_rounds + 1):
            if current_round == 1:
                pairs = self.pair_players_randomly(players_in_tournament)
            else:
                pairs = self.pair_players_by_tournament_score(
                    players_in_tournament
                )
            matches = self.create_matches(pairs)

            round_name = Round(
                f"Round {current_round}/{total_rounds}",
                f"{matches}, end_time = None")
            print(round_name)

            for match in matches:  # Boucle de mise à jour de resultat
                choice = self.tournament_view.get_result_option(match)
                self.update_players_score(match, choice, players_in_tournament)

            # Mise a jour de la date de fin du round
            round_name.end_time = self.tournament_view.finish_round()

            # Mise a jour de la date de fin du tournoi
            if current_round == total_rounds:
                new_tournament_data["end_date"] = round_name.end_time
            print(matches)

            # Ajout du round au tournoi
            new_tournament_data["rounds"].append(round_name.to_json())
            all_tournaments = self.load_tournament_from_json('/Users/guwoop/'
                                                             'Documents/'
                                                             'chess_tournament'
                                                             '/data/'
                                                             'tournament_list'
                                                             '.json')
            new_tournament_data = Tournament(**new_tournament_data).to_json()

            # Si le tournoi existe déjà, le mettre à jour
            for i, tournament in enumerate(all_tournaments):
                if tournament['name'] == new_tournament_data['name']:
                    all_tournaments[i] = new_tournament_data
                    break
            else:
                all_tournaments.append(new_tournament_data)
            self.save_tournament_to_json(all_tournaments, '/Users/guwoop/'
                                         'Documents/chess_tournament/'
                                         'data/tournament_list.json')

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

    # Algorythme de pairage apres le premier round
    def pair_players_by_tournament_score(self, players_in_tournament, matches):
        number_of_matches_to_play = math.floor(len(players_in_tournament) / 2)
        players_available = players_in_tournament.copy()
        players_available = sorted(
            players_available, key=lambda player: player["score"], reverse=True
            )

        pairs = []
        for i in range(number_of_matches_to_play):
            player1 = players_available.pop(0)
            perfect_match = None
            for player2 in players_available:
                if not any((player1, player2) in match or (player2, player1)
                           in match for match in matches):
                    perfect_match = players_available.pop(
                        players_available.index(player2)
                        )
                    break

            if perfect_match:
                pair = [player1, perfect_match]
                pairs.append(pair)

# Si aucun match parfait n'est trouvé,
# on prend le joueur suivant disponible (on prend un match random inédit)
            else:
                player2 = players_available.pop(0)
                pair = [player1, player2]
                pairs.append(pair)
        return pairs

    def create_new_tournament(self, players_in_tournament):
        file_path = "/Users/guwoop/Documents/"
        "chess_tournament/data/tournament_list.json"
        all_tournaments = self.load_tournament_from_json(file_path)
        new_tournament_data = self.tournament_view.input_tournament_data(
            players_in_tournament
            )
        all_tournaments.append(new_tournament_data)
        self.save_tournament_to_json(all_tournaments, file_path)
        return new_tournament_data

    # Liste des joueurs participant au tournoi
    def participating_players_list(self):
        existing_players = self.player_controller.load_players_from_json(
            "/Users/guwoop/Documents/chess_tournament/data/player_list.json")
        players_in_tournament = []

        while True:  # On ajoute les joueurs au tournoi avec leur chess_id
            chess_id = self.player_view.chess_id_input()
            found_player = False

            for player_data in existing_players:
                if player_data['chess_id'] == chess_id:

                    # Vérifie si le joueur est déjà dans la liste
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
                # On s'assure que le nombre de joueurs ajoutés est pair
                if self.verify_pair_players(players_in_tournament):
                    break
                else:
                    print("Le nombre de joueur doit etre pair."
                          "Ajoutez un autre joueur.")

        return players_in_tournament

    def save_tournament_to_json(self, all_tournaments, file_path):
        with open(file_path, "w") as json_file:
            json.dump(all_tournaments, json_file, indent=4)

    # Charge le dernier tournoi en cours
    def load_most_recent_tournament(self, file_path):
        all_tournaments = self.load_tournament_from_json(file_path)
        sorted_tournaments = sorted(all_tournaments,
                                    key=lambda tournament:
                                    tournament['start_date'], reverse=True)
        most_recent_tournament = sorted_tournaments[0]

        if most_recent_tournament['end_date'] is None:
            new_tournament_data = Tournament(
                **most_recent_tournament).to_json()
            players_in_tournament = new_tournament_data
            ['players_in_tournament']
            total_rounds = new_tournament_data['total_rounds']
            self.run_tournament(new_tournament_data,
                                players_in_tournament, total_rounds)
        else:
            self.tournament_view.no_unfinished_tournament()

    def load_tournament_from_json(self, file_path):
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
        return a match list
        """
        matches = []
        for pair in pairs:
            player1 = pair[0]
            player2 = pair[1]

            match = ([f"{player1['name']} {player1['surname']}",
                     player1['score']],
                     [f"{player2['name']} {player2['surname']}",
                     player2['score']])
            # Liste de tuples de matchs et de liste de joueurs
            matches.append(match)
        return matches

    # Mise à jour du score des joueurs
    def update_players_score(self, match, choice, players_in_tournament):
        # Recherche du joueur 1
        player1 = next(player for player in players_in_tournament
                       if player['name'] + " " +
                       player['surname'] == match[0][0])
        # Recherche du joueur 2
        player2 = next(player for player in players_in_tournament
                       if player['name'] + " " +
                       player['surname'] == match[1][0])

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
            self.exit()
        else:
            self.menu_view.input_error()

    def verify_pair_players(self, players_in_tournament):
        return len(players_in_tournament) % 2 == 0
