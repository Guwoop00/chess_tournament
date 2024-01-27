        # Mise à jour du JSON
        with open("player_list.json", "w") as json_file:
            for player in existing_players:
                json.dump(player.__dict__, json_file)
                json_file.write('\n')


                return {
                "name" : input("Identifiants du joueur : "),
                "surname" : input("Identifiants du joueur : "),
                "date_of_birth" : input("Identifiants du joueur : "),
                "name" : input("Identifiants du joueur : ")
                }
            

    @staticmethod
    def display_new_user_success_message():
        print("Le joueur a été ajouté avec succès.")



    @classmethod
    def create_new_player(cls):
        
        cls.chess_id = input("Identifiant du joueur : ")
        
        # Charger tous les joueurs du JSON
        existing_players = Player.load_players()

        for player in existing_players:
            if player.chess_id == cls.chess_id:
                print()
                print("Ce joueur existe déjà.")
                print()
                print(player)
                print()

        else:
            return {
            "name" : input("Prénom du joueur : "),
            "surname" : input("Nom du joueur : "),
            "date_of_birth" : input("Date de naissance du joueur : "),
            "score" : input("Score du joueur : ")
            }
    print("Le joueur a été ajouté avec succès.")


    @classmethod
    def create_new_player(cls):
        
        cls.chess_id = input("Identifiant du joueur : ")
        cls.name = input("Prénom du joueur : ")
        cls.surname = input("Nom du joueur : ")
        cls.date_of_birth = input("Date de naissance du joueur : ")
        cls.score = input("Score du joueur : ")

    print("Le joueur a été ajouté avec succès.")
    
    @staticmethod    
    def matching_chess_id(chess_id):
        # Charger tous les joueurs du JSON
        existing_players = Player.load_players()

        for player in existing_players:
            if player.chess_id == chess_id:
                print()
                print("Ce joueur existe déjà.")
                print()
                print(player)
                print()
