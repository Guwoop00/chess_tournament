class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def __str__(self):
        return "{},{},{},{},{},{}".format(
            self.player1.name, 
            self.player1.surname, 
            self.player1.score, 
            self.player2.name, 
            self.player2.surname, 
            self.player2.score
        )
    def __repr__(self) :
        return "\n({} {}, {}\n{} {}, {})\n".format(
            self.player1.name, 
            self.player1.surname, 
            self.player1.score, 
            self.player2.name, 
            self.player2.surname, 
            self.player2.score
        )
    
    def as_tuple(self):
        return (self.player1.name, self.player1.surname, self.player1.score,
                self.player2.name, self.player2.surname, self.player2.score)