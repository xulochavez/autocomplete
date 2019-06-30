import time
import random
import string

from autocomplete.autocomplete import Autocomplete


def get_random_words(no_of_words, word_length=None):
    words = []
    for _ in range(no_of_words):
        word_length = word_length or random.randint(2, 12)
        words.append(''.join(random.choice(string.ascii_lowercase) for _ in range(word_length)))
    return words


def benchmark():
    for no_of_words in [1000, 10000, 100000, 1000000]:
        start_time = time.perf_counter()
        ac = Autocomplete(get_random_words(no_of_words))
        elapsed_time = time.perf_counter() - start_time
        print(f"** Creating Autocomplete instance for {no_of_words} words took {elapsed_time} secs")
        for prefix_len in range(1, 10):
            prefix = ''.join(random.choice(string.ascii_lowercase) for _ in range(prefix_len))
            elapsed_time = time_fn(ac.get, prefix=prefix)
            print(f"Autocomplete {prefix} for {no_of_words} words took {elapsed_time} seconds")


def time_fn(fn, repeats=3, **kwargs):
    elapsed_times = []
    for _ in range(repeats):
        start_time = time.perf_counter()
        fn(**kwargs)
        elapsed_times.append(time.perf_counter() - start_time)

    return min(elapsed_times)


if __name__ == '__main__':
    benchmark()


