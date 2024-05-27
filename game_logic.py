# game_logic.py
import random

class WordGame:
    def __init__(self):
        self.words = ["python", "development", "hangman", "resume", "project", "example"]
        self.max_incorrect_guesses = 6
        self.setup_game()

    def choose_word(self):
        return random.choice(self.words)

    def setup_game(self):
        self.word = self.choose_word()
        self.guessed_letters = set()
        self.incorrect_guesses = 0

    def display_word(self):
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])

    def guess_letter(self, guess):
        if guess in self.guessed_letters:
            return "already_guessed"
        elif guess in self.word:
            self.guessed_letters.add(guess)
            if all(letter in self.guessed_letters for letter in self.word):
                return "win"
            return "correct"
        else:
            self.guessed_letters.add(guess)
            self.incorrect_guesses += 1
            if self.incorrect_guesses >= self.max_incorrect_guesses:
                return "lose"
            return "incorrect"

    def get_status(self):
        return self.max_incorrect_guesses - self.incorrect_guesses, self.display_word()

# This part is optional, it can be used for testing the game logic separately
if __name__ == "__main__":
    game = WordGame()
    print(game.display_word())
    while True:
        guess = input("Guess a letter: ").lower()
        result = game.guess_letter(guess)
        status, word_display = game.get_status()
        print(word_display)
        if result == "win":
            print("You win!")
            break
        elif result == "lose":
            print(f"You lose! The word was: {game.word}")
            break
        else:
            print(f"Guesses left: {status}")
