from game.cards import Cards


class Hilo:
    """Hilo Game. 
    
    The player guesses if the next card drawn by the dealer will be higher or lower than the previous one..

    Attributes:
        cards: Cards instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score inicial is 300, Stores the player's total score..
        card (int): Stores the first number card to be shown to the user.
        next_card (int): Stores the next number card to show the user.
        higher_or_lower: Stores the letter "l" or letter "h" as the user chooses.
        play_again: Stores user response whether they want to continue playing or not.
    """

    def __init__(self):
        """Constructs a new Hilo.
        
        Args:
            self (Hilo): an instance of Hilo.
        """
        self.cards = Cards()
        self.is_playing = True
        self.score = 300
        self.card = 0
        self.next_card = 0
        self.higher_or_lower = ""
        self.play_again = ""

        

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Hilo): an instance of Hilo.
        """
        while self.is_playing:
            self.display_card()
            self.guess_next_card()
            self.display_next_card()
            self.compare_cards()
            self.display_score()
            self.get_playing_decision()

        print('Game over. Thanks for playing!')
            

    def display_card(self): 
        """.It will show first random card for the game.

        Args:
            self (Hilo): an instance of Hilo.
        """
        self.cards.shuffle()
        self.card = self.cards.value
        print(f'\nThe card is: {self.card}')
       
    def guess_next_card(self):
        """.Select the user's choice to guess whether the next card is greater or less than the first card displayed.

        Args:
            self (Hilo): an instance of Hilo.
        """
        self.higher_or_lower = ""
        while self.higher_or_lower.lower() != "h" and self.higher_or_lower.lower() != "l": 
            guess_hi_or_low = input("Higher or Lower [h/l]: ")      
            self.higher_or_lower = guess_hi_or_low.lower() 


    def display_next_card(self): 
        """. It will show next random card for the game.

        Args:
            self (Hilo): an instance of Hilo.
        """       
        self.cards.shuffle()
        self.next_card = self.cards.value
        print(f'Next card was: {self.next_card}')
        
    def compare_cards(self):
        """.Compare the first with the second side and assign score to the player depending on the choice the player has made to guess.

        Args:
            self (Hilo): an instance of Hilo.
        """
        if (self.higher_or_lower == 'l' and self.next_card < self.card ) or (self.higher_or_lower == 'h' and self.next_card > self.card ): 
            self.score += 100
        else:
            self.score -= 75
        

      
    def display_score(self):
        """. Displays the player's current score.

        Args:
            self (Hilo): an instance of Hilo.
        """
        print(f'Your score is: {self.score}')

    
    def get_playing_decision(self):
        """. Allows the user to decide whether they want to continue playing or not.

        Args:
            self (Hilo): an instance of Hilo.
        """
        self.play_again = ""
        if (self.score <= 0):
            self.is_playing = False
            return
        else:
            while  self.play_again.lower() != "y" and self.play_again.lower() != "n":
                self.play_again = input('Play again? [y/n] ')
                self.is_playing = (self.play_again.lower() == 'y')


