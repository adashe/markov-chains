"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_string = open(file_path).read()

    return text_string

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    for i in range(len(words) - 2):

        third_word = []
        third_word.append(words[i + 2])

        if (words[i], words[i + 1]) in chains:
            chains[words[i], words[i + 1]].append(words[i + 2])

        else:
            chains[(words[i], words[i + 1])] = third_word

        # chains[(words[i], words[i + 1])] = chains.get((words[i], words[i + 1]), []) + [words[i+2]]
        # chains[(words[i], words[i + 1])] = chains.get((words[i], words[i + 1]), []).append(words[i + 2])

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # chooses random key to initiate list

    first_pair = choice(list(chains.keys()))

    # finds value of first_pair and assigns it to the variable first_value

    first_value = choice(list(chains[first_pair]))

    # adds first_pair and first_value to words list

    words = words + list(first_pair) + [first_value]
    
    # begins a loop to add new keys to words list

    while True:

        # assigns next_key as the last two items in words list

        next_key = (words[-2], words[-1])

        # checks if next_key is in chains

        if next_key in chains:

            # randomly assigns one value from the next_key to next_word

            next_word = choice(list(chains[next_key]))

            # adds next_word to words list
        
            words = words + [next_word]
        
        # ends loop if next key is not in chains

        else:

            break

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
