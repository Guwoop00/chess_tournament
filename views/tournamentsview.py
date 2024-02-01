from models.player import Player
from models.tournament import Tournament

class TournamentView:
    
    @classmethod
    def select_players_for_tournament(cls):
        tournament_players = []       
        existing_players = Player.load_players_from_json()
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
    def create_new_tournament(cls):        
        tournament_players = cls.select_players_for_tournament()
        tournament_data = {
            "name": input("Nom du tournoi : "),
            "place": input("Lieu du tournoi : "),
            "start_date": input("Début du tournoi : "),
            "end_date": input("Fin du tournoi : "),
            "description": input("Description : "),
            "tournament_players": [player.__dict__ for player in tournament_players],
        }
        Tournament.save_tournament_to_json(tournament_data)