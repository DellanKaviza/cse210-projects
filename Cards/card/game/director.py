from game.card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.cards = []
        self.is_playing = True
        self.score = 0
        self.total_score = 300
        self.decision = ""

        for i in range(2):
            card = Card()
            self.cards.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            
            self.do_updates()
            self.do_outputs()
            self.get_inputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        play_again = input("Play Again? [y/n] ")

        self.is_playing = (play_again == "y")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        for i in range(len(self.cards)):
            card = self.cards[i]
            card.roll()
        

    def do_outputs(self):
        """Displays the card and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.cards)):
            card = self.cards[i]
            values += f"{card.value} "

        value2 = self.cards[0].value
        value3 = self.cards[1].value


        print(f"The card is: {value2}")
        guess_value = input("Higher or Lower? [h/l] ")
        self.decision = (guess_value)

        if self.decision == "h" and value3 > value2:
            self.total_score +=  100
        elif self.decision == "l" and value3 < value2:
            self.total_score +=  100
        elif self.decision == "h" and value3 < value2:
            self.total_score -=  75
        elif self.decision == "l" and value3 > value2:
            self.total_score -=  75
            pass
            

        # print(f"You rolled: {values}")
        print(f"Next Card was: {value3}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)