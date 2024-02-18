from datetime import datetime

class Round:
    def __init__(self, name, matches, end_time = None):
        self.name = name
        self.matches = matches
        self.end_time = end_time
        self.start_time = datetime.now().strftime(f"%H:%M:%S le %d-%m-%Y")

    def __str__(self):
        if self.end_time is None:
            return f"{self.name},{self.start_time}. {self.matches}"
        else:
            return f"{self.name}, {self.start_time} au {self.end_time}. {self.matches}"

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
    