from typing import Any, Dict, List, Tuple


class Match:
    def __init__(self, player1: Dict[str, Any], player2: Dict[str, Any]):
        """
        Initialise un objet Match avec deux joueurs.

        Args:
            player1 (dict): Dictionnaire représentant le premier joueur.
            player2 (dict): Dictionnaire représentant le deuxième joueur.
        """
        self.player1_name: str = f"{player1['name']} {player1['surname']}"
        self.player1_score: float = player1["score"]
        self.player2_name: str = f"{player2['name']} {player2['surname']}"
        self.player2_score: float = player2["score"]

    def __str__(self) -> str:
        """
        Retourne une représentation en chaîne de caractères du match.

        Returns:
            str: Représentation en chaîne de caractères du match.
        """
        return f"{self.player1_name} ({self.player1_score}) vs {self.player2_name} ({self.player2_score})"

    def __repr__(self) -> str:
        """
        Retourne une représentation en chaîne de caractères du match.

        Returns:
            str: Représentation en chaîne de caractères du match.
        """
        return f"{self.player1_name} ({self.player1_score}) vs {self.player2_name} ({self.player2_score})"

    def update_scores(self, match_result_choice: str) -> None:
        """
        Met à jour les scores des joueurs en fonction du résultat du match.

        Args:
            match_result_choice (str): Choix du joueur pour le résultat du match.

        Raises:
            ValueError: Si le choix pour le résultat du match est invalide.
        """
        if match_result_choice == "1":
            self.player1_score += 1
        elif match_result_choice == "N":
            self.player1_score += 0.5
            self.player2_score += 0.5
        elif match_result_choice == "2":
            self.player2_score += 1
        elif match_result_choice == "Q":
            exit()
        else:
            raise ValueError("Choix invalide pour le résultat du match.")

    def to_tuple(self) -> Tuple[List[Any], List[Any]]:
        """
        Convertit le match en un tuple de tuples contenant les noms et les scores des joueurs.

        Returns:
            tuple: Tuple contenant les noms et les scores des joueurs.
        """
        return (
            [self.player1_name, self.player1_score],
            [self.player2_name, self.player2_score]
        )
