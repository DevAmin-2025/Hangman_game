# Hangman Game

This is a Python implementation of the classic Hangman game. The game selects a random word from a list of words, and the player attempts to guess the word one letter at a time. The player has a limited number of turns to guess the word correctly.

## Features

- Random word selection from a preprocessed list of words.
- User-friendly interface with color-coded feedback.
- Input validation to handle invalid guesses.
- Limited number of turns for added challenge.
- Clear and engaging progress display.

## Requirements

- Python 3.x
- termcolor module

## Code Overview

### Hangman Class
The Hangman class handles the main logic of the game. It includes methods for loading words, evaluating user input, displaying progress, and managing the game loop.

- `load_words(path: str) -> list`: Loads words from the given JSON file.
- `eval_user_input(user_guess: str) -> str`: Evaluates the user's input.
- `show_progress() -> int`: Displays the current progress of the guessed word.
- `show_initial_map()`: Displays the initial state of the word with unguessed characters.
- `play()`: Main function to run the Hangman game.

### Data Preprocessing
The `preprocess_data.py` script preprocesses the word frequency data and saves it to a JSON file.

- `build_data(path: str, min_word_len: int, total_words: int) -> list`: Builds a list of words from a file, filtering by minimum word length and selecting the most frequent words.
- `save_words(words: list, output_path: str)`: Saves a list of words to a JSON file.

### Utilities
The `utils.py` script contains utility functions for printing color-coded feedback.

## Usage

1. **Clone the Repository**: Open your terminal and run the following command to clone the repository:
```bash
git clone https://github.com/your-username/your-repo.git
```
Replace your-username and your-repo with the actual GitHub username and repository name.

2. Navigate to project directory and add the directory to `PYTHONPATH`.
```bash
cd Hangman_game
export PYTHONPATH=$(pwd)
```
3. Install any necessary package from `requirements.txt` file.
```bash
pip install -r requirements.txt
```
3. Preprocess the data to build the list of words (this is required only for the first time). Run the following script:
```bash
python src/preprocess_data.py
```
4. To start the game, run the main script:
```bash
python src/main.py
```
