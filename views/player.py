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
    def empty_json_print():
        print("Le fichier JSON est vide.")

    @staticmethod
    # Affiche la liste des joueurs triée par nom
    def display_player_list(all_players):
        sorted_players = sorted(all_players, key=lambda player:
                                (player['surname'], player['name'],
                                 player['chess_id']))
        for player in sorted_players:
            print(f"\nNom: {player['name']}"
                  f"\nPrénom: {player['surname']}"
                  f"\nIdentifiant d'échecs: {player['chess_id']}"
                  f"\nDate de naissance: {player['date_of_birth']}"
                  f"\nScore: {player['score']}\n")

    def add_players(self):
        while True:
            if not self.ask_to_add_another_player():
                break

    @staticmethod
    def ask_to_add_another_player():
        print("Voulez-vous ajouter un autre joueur ?")
        return input("Oui/Non : ").lower() == "oui"
