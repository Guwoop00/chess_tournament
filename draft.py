class Menu:

    @classmethod
    def display_menu(cls, title, options): 
        print()
        print(title)
        print("********************")
        for i, option in enumerate(options, start=1):
            print(f"[{i}] {option}")
        print("********************")
        return cls.get_user_choice()

    @classmethod
    def get_user_choice(cls):
        return int(input("Quel est votre choix ? : "))




class PlayerView:

    @staticmethod
    def input_player(all_players):
            
            chess_id = PlayerView.player_exists()
            for player in all_players:
                if player.chess_id == chess_id:
                    print("Ce joueur existe déjà.")
            
                else:
                    name = input("Prénom du joueur : ")
                    surname = input("Nom du joueur : ")
                    chess_id = input("Identifiant du joueur : ")
                    date_of_birth = input("Date de naissance du joueur : ")
                
                return {'name': name, 'surname': surname, 'chess_id': chess_id, 'date_of_birth': date_of_birth}
    
    def player_exists(players):
        chess_id = input("Identifiant du joueur : ")
        for player in players:
            if player.chess_id == chess_id:
                return True
        return False
    
    def display_all_players(all_players):
        
        print("\nListe des joueurs:\n")

        for player in all_players:
            print(f"{player}\n")


class TournamentView:
    
    @classmethod
    def select_players_for_tournament():
        tournament_players = []       
        while True:
            chess_id = input("Quel est l'identifiant du joueur : ")
            found_player = False
            for player in existing_players:
                if player.chess_id == chess_id:
                    tournament_players.append(player)
                    print(f"{player.name} {player.surname} a été ajouté au tournoi.")
                    found_player = True
                    break  
            if not found_player:
                print("Joueur non trouvé. Veuillez entrer un identifiant valide.")
            else:
                add_more = input("Voulez-vous ajouter un autre joueur (oui/non) : ")
                if add_more.lower() != "oui":
                    break

        return tournament_players

    @classmethod
    def create_new_tournament(cls, tournament_players):        
        tournament_data = {
            "name": input("Nom du tournoi : "),
            "place": input("Lieu du tournoi : "),
            "start_date": input("Début du tournoi : "),
            "end_date": input("Fin du tournoi : "),
            "description": input("Description : "),
            "tournament_players": [player.__dict__ for player in tournament_players],
        }
        return tournament_data
import json

from models.player import Player

class Tournament:
    def __init__(self, name, place, start_date, end_date, description, players_in_tournament):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.description = description        
        self.players_in_tournament = []

    def __str__(self):
        return f"{self.name}, du {self.start_date} au {self.end_date}"
    
    @staticmethod    
    def save_tournament_to_json(all_tournaments):
        with open(file_path, "w") as json_file:
            for tournament in all_tournaments:
                tournament_dict = {
                    'name': tournament.name,
                    'place': tournament.place,
                    'start_date': tournament.start_date,
                    'end_date': tournament.end_date,
                    'description': tournament.description,
                    'players_in_tournament': tournament['players_in_tournament']
                }
                all_tournaments.append(tournament_dict)
                json.dump(tournament_dict, json_file)
                json_file.write('\n')

    @classmethod    
    def load_tournaments_from_json(cls, file_path):
        all_tournaments = []
        with open(file_path, "r") as json_file:
            for line in json_file:
                tournament_data = json.loads(line)                
                all_tournaments.append(tournament)

        print("\nListe des joueurs:\n")
        for tournament in all_tournaments:
            print(f"{tournament}\n")

file_path = "/Users/guwoop/Documents/chess_tournament/data/tournament_list.json"

class Player:
    def __init__(self, name, surname, chess_id, date_of_birth, score=0):
        self.name = name
        self.surname = surname
        self.chess_id = chess_id
        self.date_of_birth = date_of_birth
        self.score = score

    def __str__(self):
        return f"{self.name} {self.surname} {self.chess_id} {self.date_of_birth}"
    
    def to_dict(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'chess_id': self.chess_id,
            'date_of_birth': self.date_of_birth,
            'score': self.score
        }
    
    import json
from models.player import Player
from views.playersview import PlayerView


class PlayerController:
    
    @staticmethod
    def create_new_player(all_players):
        player_data = PlayerView.input_player(all_players)
        new_player = Player(**player_data)
        return new_player

    @staticmethod
    def save_players_to_json():
        with open("data/tournament_list.json", "w") as json_file:
                json.dump(json_file)
                json_file.write('\n')   

    @classmethod    
    def load_players_from_json(cls, file_path):
        all_players = []
        with open(file_path, "r") as json_file:
            for line in json_file:
                player_data = json.loads(line)
                player = cls(**player_data)
                all_players.append(player)
        
        return all_players

if __name__ == "__main__":
     PlayerController.create_new_player()



         def main_menu(self):
        main_menu_options = ["Nouveau tournoi", "Gestion des joueurs", "Quitter le programme"]
        choice = self.menu_view.display_menu("Bienvenue au tournoi d'échecs :", main_menu_options)
        
        while choice != 3:
             
            if choice == 1:
                self.tournament_controller.create_new_tournament()

            elif choice == 2:
                player_menu_options = ["Nouveau joueur", "Afficher les joueurs", "Revenir au choix précédent"]
                sub_choice = self.menu_view.display_menu("Bienvenue au tournoi d'échecs :", player_menu_options)

                if sub_choice == 1:
                    self.player_controller.create_new_player()

                elif sub_choice == 2:
                    file_path = "/Users/guwoop/Documents/chess_tournament/data/player_list.json"
                    self.player_controller.load_players_from_json(file_path)

                elif sub_choice == 3:
                    self.main_menu()

                else:
                    print("Choix invalide. Veuillez réessayer.")
                

            else:
                print("Choix invalide. Veuillez réessayer.")
            break
            
        print("Programme terminé.")


    def load_players_from_json(self, file_path):
        all_players = []
        with open(file_path, "r") as json_file:
            file_content = json_file.read()
            if file_content.strip(): 
                player_data_list = json.loads(file_content)
                for player_data in player_data_list:
                    player = Player(**player_data)
                    all_players.append(player)
        return all_players