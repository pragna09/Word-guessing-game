# main.py
import tkinter as tk
from tkinter import messagebox
from game_logic import WordGame

class WordGuessingGameGUI:
    def __init__(self, master):
        self.master = master
        master.title("Word Guessing Game")
        
        self.game = WordGame()

        self.label = tk.Label(master, text="Welcome to the Word Guessing Game!", font=("Arial", 14))
        self.label.pack(pady=10)

        self.word_label = tk.Label(master, text=self.game.display_word(), font=("Arial", 18))
        self.word_label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(master, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=10)

        self.status_label = tk.Label(master, text=f"You have {self.game.max_incorrect_guesses} incorrect guesses left.", font=("Arial", 12))
        self.status_label.pack(pady=10)

        self.replay_button = tk.Button(master, text="Play Again", command=self.setup_game)
        self.replay_button.pack(pady=10)
        self.replay_button.pack_forget()

    def setup_game(self):
        self.game.setup_game()
        self.update_gui()
        self.entry.config(state=tk.NORMAL)
        self.guess_button.config(state=tk.NORMAL)
        self.replay_button.pack_forget()

    def make_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not guess.isalpha() or len(guess) != 1:
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return

        result = self.game.guess_letter(guess)
        status, word_display = self.game.get_status()

        self.word_label.config(text=word_display)
        self.status_label.config(text=f"You have {status} incorrect guesses left.")

        if result == "already_guessed":
            messagebox.showinfo("Info", "You already guessed that letter.")
        elif result == "correct":
            if result == "win":
                messagebox.showinfo("Congratulations!", f"You guessed the word: {self.game.word}")
                self.end_game()
        elif result == "incorrect":
            if result == "lose":
                messagebox.showinfo("Game Over", f"Game over! The word was: {self.game.word}")
                self.end_game()
        elif result == "win":
            messagebox.showinfo("Congratulations!", f"You guessed the word: {self.game.word}")
            self.end_game()

    def update_gui(self):
        status, word_display = self.game.get_status()
        self.word_label.config(text=word_display)
        self.status_label.config(text=f"You have {status} incorrect guesses left.")

    def end_game(self):
        self.replay_button.pack()
        self.guess_button.config(state=tk.DISABLED)
        self.entry.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    game_gui = WordGuessingGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
