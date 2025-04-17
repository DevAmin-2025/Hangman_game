import json
import random

random.seed(41)

from src.utils import (print_guessed, print_info, print_lose, print_unguessed,
                       print_win)


class Hangman:
    CACHE_FILE = './src/data/preprocessed_words.json'

    def __init__(self):
        """
        A class to represent the Hangman game.

        Attributes
        ----------
        CACHE_FILE : str
            Path to the JSON file containing preprocessed words.
        guesses : str
            User's guessed characters.
        words : list
            List of preprocessed words.
        random_word : str
            The word to be guessed in the game.
        turns : int
            Number of turns available to the user.

        Methods
        -------
        load_words(path: str) -> list:
            Load words from the given JSON file.

        eval_user_input(user_guess: str) -> str:
            Evaluate the user's input.

        show_progress() -> int:
            Display the current progress of the guessed word.

        show_initial_map():
            Display the initial state of the word with unguessed characters.

        play():
            Main function to run the Hangman game.
        """
        self.guesses = ''  # user's inputs will be added to this string
        self.words = self.load_words(self.CACHE_FILE)
        self.random_word = random.choice(self.words)
        self.turns = len(self.random_word) + 2

    def load_words(self, path: str) -> list:
        """
        Load words from the given JSON file.

        :param path: The path to the JSON file containing preprocessed words.
        :return: A list of words loaded from the JSON file.
        """
        with open(path) as f:
            return json.load(f)

    def eval_user_input(self, user_guess: str) -> str:
        """
        Evaluate the user's input.

        :param user_guess: The character guessed by the user.
        :return: Status indicating the result of the evaluation.
        """
        if user_guess.lower() == 'quit':
            return 'break'
        elif not user_guess.isalpha():
            print_info('Invalid input.\n')
            return 'continue'
        elif not len(user_guess) == 1:
            print_info('You should only enter ONE character from the alphabet.\n')
            return 'continue'
        elif user_guess in self.guesses:
            print_info('You already entered this letter.')
            print_info('Try another one!\n')
            return 'continue'

    def show_progress(self) -> int:
        """
        Display the current progress of the guessed word.

        :return: Number of unguessed characters remaining.
        """
        failed = 0  # determine if the word is fully guessed, zero means the user has won
        for ind, char in enumerate(self.random_word):
            if ind == 0 or ind == len(self.random_word) - 1:
                print_guessed(f' {char} ')
            elif char in self.guesses:
                print_guessed(f' {char} ')
            else:
                print_unguessed(' _ ')
                failed += 1
        return failed

    def show_initial_map(self):
        """
        Display the initial state of the word with unguessed characters.
        """
        for i in range(len(self.random_word)):
            if i == 0 or i == len(self.random_word) - 1:
                print_guessed(f' {self.random_word[i]} ')
            else:
                print_unguessed(' _ ')
        print()

    def play(self):
        """
        Main function to run the Hangman game.
        """
        self.show_initial_map()
        while True:
            user_guess = input("Enter a letter (type 'quit' to exit): ")
            eval_result = self.eval_user_input(user_guess)
            if eval_result == 'break':
                break
            elif eval_result == 'continue':
                self.show_progress()
                print()
                continue

            self.guesses += user_guess.lower()

            if user_guess.lower() not in self.random_word[1:-1]:
                self.turns -= 1
                if self.turns == 0:
                    print_lose('You lose\n')
                    print_info(f'The word was: {self.random_word}')
                    break
                print_info('Wrong letter')
                print_info(f'You have {self.turns} more guesses.\n')
                self.show_progress()
                print()
                continue

            failed = self.show_progress()
            print()
            if failed == 0:
                print_win('\nCongratulations! You Win')
                break


if __name__ == '__main__':
    game = Hangman()
    game.play()
