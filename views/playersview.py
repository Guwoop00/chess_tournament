from models.player import Player

class PlayerView:
    
    @classmethod
    def create_new_player(cls):
        chess_id = input("Identifiant du joueur : ")
        existing_players = Player.load_players_from_json()

        if cls.player_exists(chess_id, existing_players):
            print("Ce joueur existe déjà.")
            return

        new_player_data = cls.get_player_data(chess_id)
        existing_players.append(Player(**new_player_data))

        Player.save_players_to_json(existing_players)
        print("Le joueur a été ajouté avec succès.")

    @staticmethod
    def player_exists(chess_id, players):
        for player in players:
            if player.chess_id == chess_id:
                return True
        return False

    @staticmethod
    def get_player_data(chess_id):
        return {
            "name": input("Prénom du joueur : "),
            "surname": input("Nom du joueur : "),
            "date_of_birth": input("Date de naissance du joueur : "),
            "chess_id": chess_id,
        }