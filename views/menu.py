class MenuViews:

    @classmethod
    def display_menu(cls, title, options):
        """
        Display menus.

        Args:
            title (str): The title of the menu.
            options (list of str): List of menu options.

        Returns:
            int: User choice.
        """
        print()
        print(title)
        print("********************")
        # Affiche les options du menu
        for i, option in enumerate(options, start=1):
            print(f"[{i}] {option}")
        print("********************")

        while True:
            try:
                choice = int(input("Quel est votre choix: "))
                if 1 <= choice <= len(options):
                    return choice
                else:
                    print(
                        "Choix invalide. Merci d'entrer un nombre" "entre 1 et ",
                        len(options),
                    )
            except ValueError:
                print("Choix invalide. Merci de rentrer un nombre valide.")

            return cls.get_user_choice()

    @classmethod
    def get_user_choice(cls):
        return int(input("Quel est votre choix ? : "))

    @staticmethod
    def player_list_print():
        print("\nListe des joueurs:\n")

    @staticmethod
    def tournament_list_print():
        print("\nListe des tournois:\n")

    @staticmethod
    def input_error():
        print("Input error, entrez une option valide ! ")

    @staticmethod
    def main_menu_options():
        return [
            "Gestion des tournois",
            "Gestion des joueurs",
            "Rapports",
            "Quitter le programme",
        ]

    @staticmethod
    def tournament_menu_options():
        return [
            "Nouveau tournoi",
            "Reprendre le dernier tournoi",
            "Retour au menu principal",
        ]

    @staticmethod
    def players_menu_options():
        return ["Nouveau joueur", "Retour au menu principal"]

    @staticmethod
    def rapports_menu_options():
        return [
            "Afficher les tournois",
            "Afficher les joueurs",
            "Retour au menu principal",
        ]
