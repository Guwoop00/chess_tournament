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
        all_players = self.player_controller.load_players_from_json(
            "/Users/guwoop/Documents/chess_tournament/data/player_list.json"
        )
        all_tournaments = self.tournament_controller.load_tournament_from_json(
         "/Users/guwoop/Documents/chess_tournament/data/tournament_list.json"
        )
        main_menu_options = [
            "Gestion des tournois",
            "Gestion des joueurs",
            "Quitter le programme"
        ]
        choice = self.menu_view.display_menu(
            "Bienvenue au tournoi d'échecs :",
            main_menu_options
        )

        if choice == 1:  # Gestion des tournois
            tournament_menu_options = [
                "Nouveau tournoi",
                "Afficher les tournois",
                "Reprendre le dernier tournoi",
                "Retour au menu principal"
            ]
            tournament_sub_choice = self.menu_view.display_menu(
                "Bienvenue au tournoi d'échecs :", tournament_menu_options
            )

            if tournament_sub_choice == 1:
                self.player_view.display_player_list(all_players)
                self.tournament_controller.launch_tournament()
            elif tournament_sub_choice == 2:
                self.menu_view.tournament_list_print()
                self.tournament_view.display_tournament_list(all_tournaments)
            elif tournament_sub_choice == 3:
                self.tournament_controller.load_most_recent_tournament(
                    "/Users/guwoop/Documents/chess_tournament/data/"
                    "tournament_list.json"
                )
            elif tournament_sub_choice == 4:
                self.main_menu()
            else:
                self.main_menu()

        elif choice == 2:  # Gestion des joueurs
            player_menu_options = [
                "Nouveau joueur",
                "Afficher les joueurs",
                "Retour au menu principal"
            ]
            player_sub_choice = self.menu_view.display_menu(
                "Bienvenue au tournoi d'échecs :", player_menu_options
            )

            if player_sub_choice == 1:
                self.player_controller.create_new_player()
            elif player_sub_choice == 2:
                self.menu_view.player_list_print()
                self.player_view.display_player_list(all_players)
            elif player_sub_choice == 3:
                self.main_menu()
            else:
                self.main_menu()

        elif choice == 3:
            exit()


if __name__ == "__main__":
    run = MainController()
    run.main_menu()
