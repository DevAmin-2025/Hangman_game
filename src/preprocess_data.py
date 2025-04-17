import json


def build_data(path: str, min_word_len: int, total_words: int) -> list:
	"""
    Build a list of words from a file, filtering by minimum word length
    and selecting the most frequent words.

    :param path: The path to the file containing words and their frequencies.
    :param min_word_len: The minimum length of words to be included.
    :param total_words: The total number of most frequent words to be selected.
    :return: A list of words filtered by length and sorted by frequency.
    """
	with open(path) as f:
		words = list()
		for i in f:
			if i.startswith('\n'):
				continue
			word, frequency = i.split(',')
			frequency = frequency.replace('\n', '')
			words.append((word, frequency))

	words = [word for word in words if len(word[0]) >= min_word_len]  # select words with specified length
	words = sorted(words, key=lambda x: int(x[1]), reverse=True)  # sort words based on frequency
	words = [word[0] for word in words]  # remove frequency
	words = words[:total_words]  # select limited number of most frequent words
	return words


def save_words(words: list, output_path: str):
	"""
    Save a list of words to a JSON file.

    :param words: The list of words to be saved.
    :param output_path: The path to the output file where the words will be saved.
    """
	with open(output_path, 'w') as f:
		json.dump(words, f)


if __name__ == '__main__':
	path = './src/data/words_frequency.txt'
	output_path = './src/data/preprocessed_words.json'
	words = build_data(path, min_word_len=5, total_words=2000)
	save_words(words, output_path)
