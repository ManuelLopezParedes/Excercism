import math
import random


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    # creación de puntos de habilidad
    def ability(self):
        dados = []
        for _ in range(4):
            dados.append(random.randint(1, 6))
        dados.remove(min(dados))
        return sum(dados)


def modifier(value):
    return math.floor((value - 10) / 2)
