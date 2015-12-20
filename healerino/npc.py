class NPC:

    """
    NPC
    """

    def __init__(self, name, hp, ap):
        self.name = name
        self._hp = hp
        self._ap = ap

    def __str__(self):
        return "{} (HP: {:>3})".format(self.name, self.hp)

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = 0 if value < 0 else value

    @property
    def ap(self):
        return self._ap

    @property
    def is_dead(self):
        return self._hp == 0

    def attack(self, target):
        target.hp -= self._ap
