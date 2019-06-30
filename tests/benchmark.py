import time
import random
import string
import contextlib

from autocomplete.autocomplete import Autocomplete, AutocompleteWithList


def get_random_words(no_of_words, word_length=None):
    words = []
    for _ in range(no_of_words):
        word_length = word_length or random.randint(2, 12)
        words.append(''.join(random.choice(string.ascii_lowercase) for _ in range(word_length)))
    return words


def benchmark():
    for no_of_words in [1000, 10000, 100000, 1000000]:
        with time_and_log(f"* Creating {no_of_words} random words took"):
            words = get_random_words(no_of_words)
        with time_and_log(f"** Creating Autocomplete instance for {no_of_words} words took"):
            ac = Autocomplete(words)
        for prefix_len in range(1, 10):
            prefix = ''.join(random.choice(string.ascii_lowercase) for _ in range(prefix_len))
            with time_and_log(f"Autocomplete {prefix} for {no_of_words} words took"):
                ac.get(prefix)

        with time_and_log(f"** Creating AutocompleteWithList instance for {no_of_words} words took"):
            ac = AutocompleteWithList(words)
        for prefix_len in range(1, 10):
            prefix = ''.join(random.choice(string.ascii_lowercase) for _ in range(prefix_len))
            with time_and_log(f"AutocompleteWithList {prefix} for {no_of_words} words took"):
                ac.get(prefix)


@contextlib.contextmanager
def time_and_log(msg):
    start_time = time.perf_counter()
    yield
    elapsed_time = time.perf_counter() - start_time
    print(f"{msg} took {elapsed_time} seconds")


def time_fn(fn, repeats=3, **kwargs):
    elapsed_times = []
    for _ in range(repeats):
        start_time = time.perf_counter()
        fn(**kwargs)
        elapsed_times.append(time.perf_counter() - start_time)

    return min(elapsed_times)


def sanity_check():
    words = get_random_words(100000)
    ac = Autocomplete(words)

    for _ in range(20):
        prefix = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 10)))
        completions = ac.get(prefix)

        print(f"Autocomplete for {prefix} with 10000 randon words returned:\n{completions}")

if __name__ == '__main__':
    #sanity_check()
    benchmark()


