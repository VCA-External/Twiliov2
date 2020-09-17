import random
import string
import time


def get_random_string(length):
    letters = string.ascii_uppercase
    result_str = ''.join(random.choice(letters)
                         for i in range(length)) + str(time.time())[-5:-2]
    return result_str
