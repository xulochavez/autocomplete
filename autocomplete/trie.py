


class Trie:

    def __init__(self, words=[]):
        self.root = Node(char=None, is_word_end=False)

        for word in words:
            self.add_word(word)

    def add_word(self, word):
        self.root.add(word)

    def __repr__(self):
        return str(self.root)

    def __contains__(self, item):
        return item in self.root

    def get_words(self, prefix):
        prefix_leaf_child = self.root._get_prefix_child(prefix)
        if prefix_leaf_child:
            return set(prefix_leaf_child.get_words(prefix[:-1]))


class Node:

    def __init__(self, char, is_word_end):
        self.char = char
        self.is_word_end = is_word_end
        self.children = {}

    def _split(self, word):
        char, remainder = word[0], word[1:]
        return char, remainder

    def _get_or_create_child(self, char, is_word_end):
        return self.children.setdefault(char, Node(char=char, is_word_end=is_word_end))

    def add(self, word):
        if not word:
            return

        char, remainder = self._split(word)
        is_word_end = False if remainder else True

        child = self._get_or_create_child(char, is_word_end)
        if remainder:
            child.add(remainder)

    def __contains__(self, item):
        if not item:
            return False

        char, remainder = self._split(item)
        if char not in self.children:
            return False
        elif remainder:
            return remainder in self.children[char]
        else:
            return True

    def _get_prefix_child(self, prefix):
        char, remainder = self._split(prefix)
        child = self.children.get(char, None)

        if not child:
            return None
        elif remainder:
            return child._get_prefix_child(remainder)
        else:
            return child

    def get_words(self, prefix):
        if self.is_word_end and self.char:
            words = [prefix + self.char]
        else:
            words = []

        for child in self.children.values():
            words.extend(child.get_words(prefix=prefix+self.char))
        return words

    def __repr__(self):
        return "<" + ', '.join(f"{k}: {val}" for k, val in self.children.items()) + ">"







