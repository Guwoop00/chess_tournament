from typing import Tuple


class Match:
    def __init__(self, player1: Tuple[str, float], score1: float,
                 player2: Tuple[str, float], score2: float) -> None:
        """
        Initializes a Match object with two players represented by tuples.

        Args:
            player1 (Tuple[str, float]): Tuple representing the first player with their name and score.
            score1 (float): Score of the first player.
            player2 (Tuple[str, float]): Tuple representing the second player with their name and score.
            score2 (float): Score of the second player.
        """
        self.players = ([player1, score1], [player2, score2])

    def __str__(self) -> str:
        """
        Returns a string representation of the match.

        Returns:
            str: String representation of the match.
        """
        return ("[{} {}, {}], [{} {}, {}])".format(
            self.players[0][0][0], self.players[0][0][1], self.players[0][1],
            self.players[1][0][0], self.players[1][0][1], self.players[1][1]))

    def __repr__(self) -> str:
        """
        Returns a string representation of the match.

        Returns:
            str: String representation of the match.
        """
        return ("[{} {}, {}], [{} {}, {}])".format(
            self.players[0][0][0], self.players[0][0][1], self.players[0][1],
            self.players[1][0][0], self.players[1][0][1], self.players[1][1]))

    def to_json(self) -> str:
        """
        Convert the match data to JSON format.

        Returns:
            str: JSON representation of the match.
        """
        return ("[{} {}, {}], [{} {}, {}])".format(
            self.players[0][0][0], self.players[0][0][1], self.players[0][1],
            self.players[1][0][0], self.players[1][0][1], self.players[1][1]))
