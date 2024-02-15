from datetime import datetime

class Round:
    def __init__(self, name, matchs, start_time = datetime.now().strftime(f"à %H:%M:%S le %d-%m-%Y"), end_time=None):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.matchs = matchs

    def __str__(self):
        if self.end_time is None:
            return f"{self.name},{self.start_time}. {self.matchs}"

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
    