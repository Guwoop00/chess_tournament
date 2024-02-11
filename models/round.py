import time


class Round:
    def __init__(self, name, matches, start_time=time.time(), end_time=None):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.matches = matches

    def __str__(self):
        out_str = ""
        if self.end_time is None:
            out_str += f"{self.name}, débuté à {self.start_time}\nEN COURS\n"
        else:
            out_str += f"{self.name} : {self.start_time} - {self.end_time}\n"
        for match in self.matches:
            out_str += f"{str(match)}\n"
        return out_str

    def to_json(self):
        turn = {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": []
        }
        for match in self.matches:
            turn['matches'].append(match.to_json())

        return turn
    
    def create_match(self, player_1, player_2):
        match = (
            f"{player_1['last_name']}, {player_1['first_name']}",
            player_1["score"],
            f"{player_2['last_name']}, {player_2['first_name']}",
            player_2["score"]
        )
        self.matches.append(match)