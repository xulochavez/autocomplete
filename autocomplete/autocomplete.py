
from autocomplete.trie import Trie


WORDS = ['mean', 'algae', 'alumni', 'table', 'tables', 'meat', 'mother', 'mouse', 'motherhood']


class Autocomplete:
    def __init__(self, words=None):
        self.trie = Trie(words or WORDS)

    def get(self, prefix):
        return self.trie.get_words(prefix)


class AutocompleteWithList:
    def __init__(self, words=None):
        self.words = words or WORDS

    def get(self, prefix):
        return set(w for w in self.words if w.startswith(prefix))

if __name__ == '__main__':
    print(Autocomplete().get('m'))
