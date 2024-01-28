from playersmodels import Player
from models.tournament import Tournament
from views.menu import ViewMenu
from views.playerviews import PlayerView

class MainController:

    @classmethod
    def run(cls):
        main_menu_options = ["Nouveau tournoi", "Gestion des joueurs", "Quitter le programme"]
        choice = ViewMenu.display_menu("Welcome to chess tournament:", main_menu_options)
        
        while choice != 3:
            
            if choice == 1:
                Tournament.create_new_tournament()

            elif choice == 2:
                
                # Gestion des joueurs
                player_menu_options = ["Nouveau joueur", "Afficher les joueurs", "Revenir au choix précédents"]
                player_choice = ViewMenu.display_menu("Player menu:", player_menu_options)

                if player_choice == 1:
                    PlayerView.create_new_player(cls)

                elif player_choice == 2:
                    Player.display_all_players("/Users/guwoop/Documents/chess_tournament/data/player_list.json")

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
