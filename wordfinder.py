from random import choice
"""Word Finder: finds random words from a dictionary."""

class WordFinder:
    def __init__(self, words_file):
        f = open(words_file, 'r')
        self.words = f.read().split('\n')
        f.close()

        for word in self.words:
            if word[0] == "#":
                self.words.remove(word)

    def random(self):
        return choice(self.words)
