class MenuViews:

    @classmethod
    def display_menu(cls, title, options):
        print()
        print(title)
        print("********************")
        # Affiche les options du menu
        for i, option in enumerate(options, start=1):
            print(f"[{i}] {option}")
        print("********************")
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

    def input_error(self):
        print("Input error, entrez une option valide ! ")
