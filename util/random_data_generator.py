import random
import string
import time


class RandomDataGenerator:
    def __init__(self):
        self.generator_options = [self.random_string, self.random_int]

    def get_random(self):
        return random.choice(self.generator_options)()

    def random_string(self, length=16):
        return "".join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(length))

    def random_int(self):
        return random.randint(0, 999)
