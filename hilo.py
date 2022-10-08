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
class Game:
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
                game.player.setPoints(self.rightGuessPoints)
            else:
                game.player.setPoints(self.wrongGuessPoints)
        else:
            if revealedCard > currentCard:
                game.player.setPoints(self.rightGuessPoints)
            else:
                game.player.setPoints(self.wrongGuessPoints)

if __name__ == "__main__":
    #initiate Game class with the parameters for:
    # Initial points (300)
    # Right guess points (100) 
    # Wrong guess points (-75) 
    # Number of cards (13)
    game = Game(300, 100, -75, 13)

    answer = "y"
    while answer.lower()== "y":
        print("")
        print(f"The card is: {game.deck.currentCard}")
        guess = input("Higher or lower? [h/l] ")
        game.calculateGuess(guess)

        if (game.player.points <= 0):
            print(f"Your score is: {game.player.points}")
            print("The game is over.")
            break

        print(f"Next card was: {game.deck.currentCard}")
        print(f"Your score is: {game.player.points}")

        answer = input("Play again? [y/n] ")
    else:
        print("The game is over.")

