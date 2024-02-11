from views.menu import MenuViews
from views.player import PlayerView
from views.tournament import TournamentView
from controllers.tournamentscontroller import TournamentController
from controllers.playerscontroller import PlayerController

class MainController:

    def __init__(self):
        self.menu_view = MenuViews()
        self.tournament_controller = TournamentController()
        self.player_controller = PlayerController()
        self.player_view = PlayerView()
        self.tournament_view = TournamentView()

    def main_menu(self):
        all_players = self.player_controller.load_players_from_json("/Users/guwoop/Documents/chess_tournament/data/player_list.json")
        main_menu_options = ["Nouveau tournoi", "Gestion des joueurs", "Quitter le programme"]
        choice = self.menu_view.display_menu("Bienvenue au tournoi d'échecs :", main_menu_options)

        if choice == 1:
            self.player_view.display_player_list(all_players)
            players_in_tournament = self.tournament_controller.participating_players_list()
            self.tournament_controller.create_new_tournament(players_in_tournament)
            start = self.tournament_view.start_tournament_input()
            if start == "oui":
                pairs = self.tournament_controller.pairing_players(players_in_tournament)
                self.tournament_controller.create_matchs(pairs)
            
        elif choice == 2:
            player_menu_options = ["Nouveau joueur", "Afficher les joueurs", "Retour au menu principal"]
            sub_choice = self.menu_view.display_menu("Bienvenue au tournoi d'échecs :", player_menu_options)
            if sub_choice == 1:
                self.player_controller.create_new_player()
            elif sub_choice == 2:
                self.menu_view.player_list_print()
                self.player_view.display_player_list(all_players)
            elif sub_choice == 3:
                self.main_menu()
            else:
                self.main_menu()

        elif choice == 3:
            exit()

if __name__ == "__main__":
    run = MainController()
    run.main_menu()