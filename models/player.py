class Player:
    def __init__(self, name, surname, chess_id, date_of_birth, score=0):
        self.name = name
        self.surname = surname
        self.chess_id = chess_id
        self.date_of_birth = date_of_birth
        self.score = score

    def __str__(self):
        return f"{self.name} {self.surname}, {self.chess_id} {self.date_of_birth} {self.score}"

    def __repr__(self):
        return f"{self.name} {self.surname} {self.chess_id} {self.date_of_birth} {self.score}"

    def to_json(self):
        """
        Convert player data to a dictionary.

        Returns:
            dict: Dictionary containing player data.
        """
        return {
            "name": self.name,
            "surname": self.surname,
            "chess_id": self.chess_id,
            "date_of_birth": self.date_of_birth,
            "score": self.score,
        }
