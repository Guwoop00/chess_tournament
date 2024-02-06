class PlayerView:

    @classmethod
    def input_player_data(cls, chess_id):
            return {
                "name": input("Prénom du joueur : "),
                "surname": input("Nom du joueur : "),
                "date_of_birth": input("Date de naissance du joueur : "),
                "chess_id": chess_id,
            }
    
    @classmethod
    def player_created(cls):
        print("Le joueur a été ajouté avec succès.")

    @classmethod
    def player_exists_output(cls):
        print("Ce joueur existe déjà.")

    @classmethod
    def chess_id_input(cls):
        chess_id = input("Identifiant du joueur : ")
        return chess_id
    
    @staticmethod
    def display_player_list(all_players):
        for player in all_players:
            print(f"{player}\n")