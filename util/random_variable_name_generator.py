import random
import string
import time


class RandomVariableNameGenerator:
    def __init__(self):
        self.generator_options = [
            self.random_string,
            self.time_based,
            self.just_id,
            self.scream,
            self.laugh,
            self.sleep,
            self.snake,
            self.repeat_letter,
            self.underscores
        ]

    def get_random(self, id):
        return random.choice(self.generator_options)(id)

    def random_string(self, id, length=16):
        return "".join(random.choice(string.ascii_letters) for i in range(length)) + str(id)

    def time_based(self, id):
        return random.choice(string.ascii_letters) + str(time.time()).replace(".", "") + str(id)

    def just_id(self, id):
        return random.choice(string.ascii_letters) + str(id)

    def scream(self, id):
        return "".join(random.choice("Aa") for i in range(id))
        
    def laugh(self, id):
        return "".join(random.choice("AaHh") for i in range(id))
        
    def sleep(self, id):
        return "".join(random.choice("Zz") for i in range(id))
    
    def snake(self, id):
        return "".join(random.choice("Ss") for i in range(id))
    
    def repeat_letter(self, id):
        return random.choice(string.ascii_letters) * id
    
    def underscores(self, id, length=16):
        return "_" * min(id * 2, random.randint(0, length)) + self.random_string(id, length)

        