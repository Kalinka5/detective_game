#  make class Health_exception to monitoring amount of lives.
class Health_exception(Exception):
    def __init__(self, health):
        self._health = health
