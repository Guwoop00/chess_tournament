from views.menusview import Menu
from views.playersview import PlayerView
from views.tournamentsview import TournamentView
from models.player import Player

class MainController:
    @classmethod
    def run(cls):
        main_menu_options = ["Nouveau tournoi", "Gestion des joueurs", "Quitter le programme"]
        choice = Menu.display_menu("Bienvenue au tournoi d'échecs :", main_menu_options)
        
        while choice != 3:
             
            if choice == 1:
                TournamentView.create_new_tournament()

            elif choice == 2:
                player_menu_options = ["Nouveau joueur", "Afficher les joueurs", "Revenir au choix précédent"]
                player_choice = Menu.display_menu("Menu joueur :", player_menu_options)

                if player_choice == 1:
                    PlayerView.create_new_player()

                elif player_choice == 2:
                    Player.load_players_from_json()

                elif player_choice == 3:
                    MainController.run()

                else:
                    print("Choix invalide. Veuillez réessayer.")
                

            else:
                print("Choix invalide. Veuillez réessayer.")
            break
            
        print("Programme terminé.")

if __name__ == "__main__":
    MainController.run()