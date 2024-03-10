from typing import List

from controllers.playerscontroller import PlayerController
from controllers.tournamentscontroller import TournamentController
from views.menu import MenuViews
from views.player import PlayerView
from views.tournament import TournamentView


class MainController:
    def __init__(self):
        self.menu_view = MenuViews()
        self.tournament_controller = TournamentController()
        self.player_controller = PlayerController()
        self.player_view = PlayerView()
        self.tournament_view = TournamentView()

    def main_menu(self):
        """
        Main menu of the program
        """
        all_players: List[dict] = self.player_controller.load_players_from_json(
            "data/player_list.json"
        )
        all_tournaments: List[dict] = (
            self.tournament_controller.load_tournament_from_json(
                "data/tournament_list.json"
            )
        )
        main_menu_options: dict = self.menu_view.main_menu_options()
        choice: int = self.menu_view.display_menu(
            "Bienvenue au tournoi d'échecs :", main_menu_options
        )

        if choice == 1:  # Gestion des tournois
            tournament_menu_options: dict = self.menu_view.tournament_menu_options()
            tournament_sub_choice: int = self.menu_view.display_menu(
                "Gestion des tournois :", tournament_menu_options
            )

            if tournament_sub_choice == 1:
                self.player_view.display_player_list(all_players)
                self.tournament_controller.launch_tournament()
            elif tournament_sub_choice == 2:
                self.tournament_controller.load_most_recent_tournament(
                    "data/tournament_list.json"
                )
            elif tournament_sub_choice == 3:
                self.main_menu()

        elif choice == 2:  # Gestion des joueurs
            player_menu_options: dict = self.menu_view.players_menu_options()
            player_sub_choice: int = self.menu_view.display_menu(
                "Gestion des joueurs :", player_menu_options
            )

            if player_sub_choice == 1:
                self.player_controller.create_new_player()
            elif player_sub_choice == 2:
                self.main_menu()

        elif choice == 3:  # Gestion des rapports
            rapports_menu_options: dict = self.menu_view.rapports_menu_options()
            player_sub_choice: int = self.menu_view.display_menu(
                "Gestion des rapports :", rapports_menu_options
            )

            if player_sub_choice == 1:
                self.menu_view.tournament_list_print()
                self.tournament_view.display_tournament_list(all_tournaments)
            elif player_sub_choice == 2:
                self.menu_view.player_list_print()
                self.player_view.display_player_list(all_players)
            elif player_sub_choice == 3:
                self.main_menu()

        elif choice == 4:
            exit()


if __name__ == "__main__":
    run = MainController()
    run.main_menu()
