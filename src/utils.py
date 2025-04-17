"""
Utility functions helping us to have different ways of printing text.
"""
from termcolor import colored


def print_guessed(text: str):
	print(colored(text, 'green', attrs=['reverse']), end='')


def print_unguessed(text: str):
	print(colored(text, 'yellow', attrs=['reverse']), end='')


def print_info(text: str):
		print(colored(text, 'white', attrs=['reverse']))


def print_win(text: str):
	print(colored(text, 'green', attrs=['reverse', 'blink']))


def print_lose(text: str):
	print(colored(text, 'red', attrs=['reverse', 'blink']))
