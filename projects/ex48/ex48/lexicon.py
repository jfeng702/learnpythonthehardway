direction = {'north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'}
verb = {'go', 'stop', 'kill', 'eat'}
stop = {'the', 'in', 'of', 'from', 'at', 'it'}
noun = {'door', 'bear', 'princess', 'cabinet'}
numbers = {}


def scan(sentence):
    # lower_case = sentence.lower()
    array_words = sentence.split()
    return [convert_number(word) for word in array_words]

    # return [('direction', words)]


def get_word(word):
    l_word = word.lower()
    if l_word in direction:
        return ('direction', word)

    elif l_word in verb:
        return ('verb', word)

    elif l_word in stop:
        return ('stop', word)

    elif l_word in noun:
        return ('noun', word)

    else:
        return ('error', word)


def convert_number(s):
    try:
        return ('number', int(s))
    except ValueError:
        return get_word(s)