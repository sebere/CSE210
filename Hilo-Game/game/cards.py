import random


class Cards:
    """Group of cards.

    The responsibility of Cards is Shuffle the cards and select one.
   
    Attributes:
        value (int): .Store the value of the card between number 1 and 13.
    """

    def __init__(self):
        """Constructs a new instance of Cards.

        Args:
            self (Cards): An instance of Cards.
        """
        self.value = 0
      

    def shuffle(self): 
        """Generates a new random value.
        
        Args:
            self (Cards): An instance of Cards.
        """
        self.value = random.randint(1, 13)
      