class Menu:

    @classmethod
    def display_menu(cls, title, options): 
        print()
        print(title)
        print("********************")
        for i, option in enumerate(options, start=1):
            print(f"[{i}] {option}")
        print("********************")
        return cls.get_user_choice()

    @classmethod
    def get_user_choice(cls):
        return int(input("Quel est votre choix ? : "))
