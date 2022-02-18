import random
import string


def random_string(length):
    random_string = ''.join((random.choice(string.ascii_letters) for x in range(length)))
    return random_string
