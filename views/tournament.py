from datetime import datetime

class TournamentView:
    @classmethod
    def input_tournament_data(cls, tournament_players):        
        new_tournament_data = {
            "name": input("Nom du tournoi : "),
            "place": input("Lieu du tournoi : "),
            "description": input("Description : "),
            "players_in_tournament": [player.__dict__ for player in tournament_players],
        }
        default_rounds = input("Nombre de tour recommandés 4 ? Oui/Non : ")
        if default_rounds.lower() == "oui":
            new_tournament_data["total_rounds"] = 4
        else:
            while True:
                total_rounds = input("Nombre de tours : ")
                if total_rounds.isdigit():
                    new_tournament_data["total_rounds"] = int(total_rounds)
                    break
                else:
                    print("Veuillez entrer un nombre entier.")        
        return new_tournament_data
    
    def get_result_option(self, match):
        valid_choices = ['1', 'N', '2', 'Q']
        while True:
            print("**************")
            print(match)
            print('**************')
            print('[1] Player 1 wins')
            print('[N] Draw')
            print('[2] Player 2 wins')
            print('**************')
            print("[Q] Back to main menu ?")
            choice = input("Qui est le vainqueur  ? ")
            if choice in valid_choices:
                return choice
            else:
                print("Invalid choice. Veuillez entrer un clé valide.")

    def added_to_tournament_input(self, player):
        print(f"{player.name} {player.surname} a été ajouté au tournoi.")

    def added_already(self, player):
        print(f"Le joueur {player.name} {player.surname} a déjà été ajouté au tournoi.")        

    def player_not_found_input(self):
        print("Joueur non trouvé. Veuillez entrer un identifiant valide.")

    def add_more_input(self):
        add_more = input("Voulez-vous ajouter un autre joueur (oui/non) : ")
        return add_more
    
    def start_tournament_input(self):
        start = input("Voulez-vous commencer le tournoi ? ")
        return start
    
    def finish_round(self):
        end_time = datetime.now().strftime(f'%H:%M:%S le %d-%m-%Y')
        print(f"Round terminé à {end_time}")
        return end_time
    
    def display_current_round(round_name):
        print(round_name)