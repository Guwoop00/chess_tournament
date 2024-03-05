from datetime import datetime


class Round:
    def __init__(self, name, matches, end_time=None):
        self.name = name
        self.matches = matches
        self.end_time = end_time
        self.start_time = datetime.now().strftime("%H:%M:%S le %d-%m-%Y")

    def __str__(self):
        if self.end_time is None:
            return f"{self.name}, démarré à {self.start_time}. Matches: {self.matches}"
        else:
            return f"{self.name}, démarré à {self.start_time}, terminé à {self.end_time}. Matches: {self.matches}"

    def to_json(self):
        """
        Convert round data to a dictionary.

        Returns:
            dict: Dictionary containing round data.
        """
        return {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": self.matches,
        }
