from autocomplete.trie import Trie
import pytest


@pytest.fixture()
def words():
    return ['mean', 'algae', 'alumni', 'table', 'tables', 'meat', 'mother', 'mouse', 'motherhood']


def test_trie(words):
    trie = Trie(words)

    print(trie)


def test_trie_supports_membership(words):
    trie = Trie(words)
    assert 'table' in trie
    assert 'al' in trie
    assert 'sup' not in trie


def test_trie_get_words(words):
    trie = Trie(words)
    assert trie.get_words('me') == set(['mean', 'meat'])

