from datetime import datetime


class TournamentView:
    @classmethod
    def input_tournament_data(cls, tournament_players):
        """
        Gathers tournament data and verifies its correctness.

        Args:
            tournament_players (list):
            List of player dictionaries participating in the tournament.

        Returns:
            dict: Dictionary containing tournament data.
        """
        new_tournament_data = {
            "name": input("Nom du tournoi : "),
            "place": input("Lieu du tournoi : "),
            "description": input("Description : "),
            "players_in_tournament": [player for player in tournament_players],
        }
        number_of_rounds = input("Nombre de tour recommandés [4] ? : ")
        if number_of_rounds.strip() == "":
            new_tournament_data["total_rounds"] = 4
        else:
            while True:
                if number_of_rounds.isdigit():
                    break  # Quitter la boucle si un entier valide est saisi
                else:
                    print("Veuillez entrer un nombre entier.")
                    number_of_rounds = input("Nombre de tour choisi ? : ")
                new_tournament_data["total_rounds"] = int(number_of_rounds)
        return new_tournament_data

    def get_result_option(self, match):
        """
        Displays the match and asks for the result.
        """
        valid_choices = ["1", "N", "2", "Q"]
        while True:
            print("**************")
            print(match)
            print("**************")
            print("[1] Player 1 wins")
            print("[N] Draw")
            print("[2] Player 2 wins")
            print("**************")
            print("[Q] Back to main menu ?")
            print("**************")
            choice = input("Qui est le vainqueur  ? ")
            if choice in valid_choices:
                return choice
            else:
                print("Invalid choice. Veuillez entrer un clé valide.")

    def added_to_tournament_input(self, player):
        print(f"{player['name']} {player['surname']} a été ajouté au tournoi.")

    def added_already(self, player):
        print(
            f"Le joueur {player['name']} {player['surname']} "
            f"a déjà été ajouté au tournoi."
        )

    def player_not_found_input(self):
        print("Joueur non trouvé. Veuillez entrer un identifiant valide.")

    def add_more_input(self):
        add_more = input("Ajouter un autre joueur ? [OK] : ")
        return add_more

    def start_tournament_input(self):
        start = input("Voulez-vous commencer le tournoi ? ")
        return start

    def finish_round(self):
        end_time = datetime.now().strftime("%H:%M:%S le %d-%m-%Y")
        print(f"Round terminé à {end_time}")
        return end_time

    def display_current_round(round_name):
        print(round_name)

    @staticmethod
    def display_tournament_list(all_tournament):
        """
        Displays the list of tournaments sorted by name and start date.

        Args:
            all_tournaments (list): List of tournament dictionaries.

        """
        sorted_tournaments = sorted(
            all_tournament, key=lambda tournament: (tournament["name"])
        )

        for tournament in sorted_tournaments:
            players_in_tournaments = tournament["players_in_tournament"]
            sorted_players_in_tournaments = sorted(
                players_in_tournaments, key=lambda player: (player["surname"])
            )
            if tournament["end_date"]:
                print(
                    f"\nNom: {tournament['name']}"
                    f"\nLieu: {tournament['place']}"
                    f"\nDate de début: {tournament['start_date']} "
                    f"Date de fin: {tournament['end_date']}"
                    f"\nTours effectués: {tournament['total_rounds']}"
                    f"\nDescription: {tournament['description']}\n"
                    f"\nListe des participants: "
                )
                for player in sorted_players_in_tournaments:
                    print(f"{player['surname']}, {player['name']}")

            else:
                print(
                    f"\nNom: {tournament['name']}"
                    f"\nLieu: {tournament['place']}"
                    f"\nDate de début: {tournament['start_date']}"
                    f"\nDate de fin: En cours"
                    f"\nTours effectués: {tournament['total_rounds']}"
                    f"\nDescription: {tournament['description']}\n"
                )
            for round in tournament["rounds"]:
                print()
                print(f"Round: {round['name']}")
                print(f"Start time: {round['start_time']}")
                print(f"End time: {round['end_time']}")
                matches = round["matches"]
                print(f"\nMatches: \n{matches}")

    @staticmethod
    def display_tournament_summary(new_tournament_json):
        """
        Displays the resume of a tournament including its name, place, start and end dates,
        total rounds, description, participants list, and rounds information.

        Args:
            new_tournament_json (dict): Dictionary containing tournament information.

        Returns:
        str: Empty string.
        """
        players_in_tournaments = new_tournament_json["players_in_tournament"]
        sorted_players_in_tournaments = sorted(
            players_in_tournaments, key=lambda player: (player["surname"])
        )
        if new_tournament_json["end_date"]:
            print(
                f"\nNom: {new_tournament_json['name']}"
                f"\nLieu: {new_tournament_json['place']}"
                f"\nDate de début: {new_tournament_json['start_date']} "
                f"Date de fin: {new_tournament_json['end_date']}"
                f"\nTours effectués: {new_tournament_json['total_rounds']}"
                f"\nDescription: {new_tournament_json['description']}\n"
                f"\nListe des participants: "
            )
            for player in sorted_players_in_tournaments:
                print(f"{player['surname']}, {player['name']}")
        else:
            print(
                f"\nNom: {new_tournament_json['name']}"
                f"\nLieu: {new_tournament_json['place']}"
                f"\nDate de début: {new_tournament_json['start_date']}"
                f"\nDate de fin: En cours"
                f"\nTours effectués: {new_tournament_json['total_rounds']}"
                f"\nDescription: {new_tournament_json['description']}\n"
            )
        for round in new_tournament_json["rounds"]:
            print()
            print(f"Round: {round['name']}")
            print(f"Start time: {round['start_time']}")
            print(f"End time: {round['end_time']}")
            matches = round["matches"]
            print(f"\nMatches: \n{matches}")
        return ""

    @staticmethod
    def no_unfinished_tournament():
        print("Aucun tournoi en cours.")

    @staticmethod
    def must_be_pair():
        print("Le nombre de joueur doit etre pair. Ajoutez un autre joueur.")

    @staticmethod
    def display_round_name(round_name):
        print()
        print(round_name)

    @staticmethod
    def display_matches(matches):
        print(matches)

    @staticmethod
    def display_resume(resume):
        print(resume)
