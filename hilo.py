import random

#This class:
# -Receives the number of cards (in this case 13)
# -Reveals the the card randomly
class Deck:
    def __init__(self, numberCards):
        self.numberCards = numberCards
        self.currentCard = 0

        self.currentCard = self.revealCard()

    def revealCard(self):
        revealedCard = random.randint(1, self.numberCards)
        while (revealedCard == self.currentCard):
            revealedCard = random.randint(1, self.numberCards)

        self.currentCard = revealedCard
        return self.currentCard

#This class:
# -Receives Player's points
# -Calculate Player's points  
class Player:
    def __init__(self, initialPoints):
        self.points = initialPoints

    def setPoints(self, points):
        self.points =  self.points + points

#This class:
# -Initiate other classes (Player and Decks)
# -Initiate the game
# -Calculates the guess
class Dealer:
    def __init__(self, initialPoints, rightGuessPoints, wrongGuessPoints, numberCards):
        self.initialPoints = initialPoints
        self.rightGuessPoints = rightGuessPoints
        self.wrongGuessPoints = wrongGuessPoints
        self.numberCards = numberCards
        self.player = Player(initialPoints)
        self.deck = Deck(numberCards)

    def calculateGuess(self, guess):
        currentCard = self.deck.currentCard
        revealedCard = self.deck.revealCard()
        if guess.lower() == "l":
            if revealedCard < currentCard:
                dealer.player.setPoints(self.rightGuessPoints)
            else:
                dealer.player.setPoints(self.wrongGuessPoints)
        else:
            if revealedCard > currentCard:
                dealer.player.setPoints(self.rightGuessPoints)
            else:
                dealer.player.setPoints(self.wrongGuessPoints)

if __name__ == "__main__":
    #initiate Dealer class with the parameters for:
    # Initial points (300)
    # Right guess points (100) 
    # Wrong guess points (-75) 
    # Number of cards (13)
    dealer = Dealer(300, 100, -75, 13)
    print("Welcome to Hilo")
    print("We will start you out with 300 points.")
    print("You will be given a number that represents a card.")
    print("You will then be asked to guess if the next")
    print("card displayed will be higher or lower than ")
    print("the card you currently see. Once you make your guess,")
    print("we will show you the next card. If your guess was")
    print("correct, we will give you 100 points. ")
    print("If you guess was incorrect, we will deduct 75 point.")
    print("We hope you will enjoy the game")
    answer = "y"
    while answer.lower()== "y":
        print("")
        print(f"The card is: {dealer.deck.currentCard}")
        guess = input("Higher or lower? [h/l] ")
        dealer.calculateGuess(guess)

        if (dealer.player.points <= 0):
            print(f"Your score is: {dealer.player.points}")
            print("Sorry, you have no more points available. The game is over.")
            break

        print(f"Next card was: {dealer.deck.currentCard}")
        print(f"Your score is: {dealer.player.points}")

        answer = input("Would you like to play again? [y/n] ")
    else:
        print("Thank you for playing. The game is now over.")

