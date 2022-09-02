#  make class exception to pace characteristic
class Health_exception(Exception):
    #  init pace, minimal pace and maximum pace
    def __init__(self, health):
        self._health = health
