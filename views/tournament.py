class TournamentView:

    @classmethod
    def input_tournament_data(cls, tournament_players):        
        tournament_data = {
            "name": input("Nom du tournoi : "),
            "place": input("Lieu du tournoi : "),
            "start_date": input("Début du tournoi : "),
            "end_date": input("Fin du tournoi : "),
            "description": input("Description : "),
            "players_in_tournament": [player.__dict__ for player in tournament_players],
        }
        return tournament_data

    
    def added_to_tournament_input(self, player):
        print(f"{player.name} {player.surname} a été ajouté au tournoi.")

    def player_not_found_input():
        print("Joueur non trouvé. Veuillez entrer un identifiant valide.")

    def add_more_input(self):
        add_more = input("Voulez-vous ajouter un autre joueur (oui/non) : ")
        return add_more
    
    def start_tournament_input(self):
        start = input("Voulez-vous commencer le tournoi ?")
        return start