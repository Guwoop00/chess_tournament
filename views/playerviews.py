from models.playersmodels import Player

class PlayerView:

    def create_new_player(cls):   

        chess_id = input("Identifiant du joueur : ")       
        existing_players = Player.load_players()

        for player in existing_players:
            if player.chess_id == chess_id:
                print()
                print("Ce joueur existe déjà.")
                print()
                print(player)
                print()
                return

        new_player_data = {
            "name" : input("Prénom du joueur : "),
            "surname" : input("Nom du joueur : "),
            "date_of_birth" : input("Date de naissance du joueur : "),
            "chess_id" : chess_id
        }
        
        # Ajouter le nouveau joueur dans le bon format
        existing_players.append(Player(**new_player_data))
        Player.save_players(existing_players)
        
        print("Le joueur a été ajouté avec succès.")
