from typing import Tuple


class Match:
    def __init__(self, player1: Tuple[str, float], player2: Tuple[str, float]):
        """
        Initializes a Match object with two players represented by tuples.

        Args:
            player1 (Tuple[str, float]): Tuple representing the first player with their name and score.
            player2 (Tuple[str, float]): Tuple representing the second player with their name and score.
        """
        self.player1: Tuple[str, float] = player1
        self.player2: Tuple[str, float] = player2

    def __str__(self) -> str:
        """
        Returns a string representation of the match.

        Returns:
            str: String representation of the match.
        """
        return f"([{self.player1[0]} {self.player1[1]}, {self.player1[2]}]), " \
               f"([{self.player2[0]} {self.player2[1]}, {self.player2[2]}])"

    def __repr__(self) -> str:
        """
        Returns a string representation of the match.

        Returns:
            str: String representation of the match.
        """
        return f"([{self.player1[0]} {self.player1[1]}, {self.player1[2]}]), " \
               f"([{self.player2[0]} {self.player2[1]}, {self.player2[2]}])"

    def to_json(self) -> str:
        """
        match data to the json file.

        Returns:
            str: Two lists in tuples.
        """
        return f"([{self.player1[0]} {self.player1[1]}, {self.player1[2]}]), " \
               f"([{self.player2[0]} {self.player2[1]}, {self.player2[2]}])"
