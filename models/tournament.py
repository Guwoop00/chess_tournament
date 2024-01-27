import json

class Tournament:
    def __init__(self, name, place, start_date, end_date, description):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.description = description

    def __str__(self):
        return f"{self.name} {self.place}\n{self.start_date}\n{self.end_date}\n{self.description}"
        
    def create_new_tournament():
        name = input("Nom du tournoi : ")
        place = input("Lieu du tournoi : ")
        start_date = input("Date de début : ")
        end_date = input("Date de fin : ")
        description = input("Description : ")
        new_tournament = Tournament(name, place, start_date, end_date, description)

        tournament_dict = {
            "name": new_tournament.name,
            "place": new_tournament.place,
            "start_date": new_tournament.start_date,
            "end_date": new_tournament.end_date,
            "description": new_tournament.description,
        }
        with open("tournament_list.json", "a") as json_file:
            json.dump(tournament_dict, json_file)
            json_file.write('\n')

    def all_tournaments_list(file_path):
        tournaments_list = []
        with open(file_path, "r") as json_file:

            for line in json_file:
                tournament_data = json.loads(line)
                tournament = Tournament(**tournament_data)
                tournaments_list.append(tournament)

        print("\nListe des tournois:\n")
        for tournament in tournaments_list:
            print(f"{tournament}\n")

file_path = "/Users/guwoop/Documents/chess_tournament/tournament_list.json"

if __name__ == "__main__":
    Tournament.all_tournaments_list(file_path)
