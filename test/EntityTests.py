import unittest
from game.classes.entity import entity
from player import player
from game.classes.fight import fight
from game.classes.augments import augment
from game.classes.enemy import enemy


class TestEntityMethods(unittest.TestCase):

    def test_init_player_currenthp(self):
        character = player("Even Steven", 20, 10, .3, .6, .15)
        stats = character.returnStats()
        self.assertEqual(stats["maxhp"], 20)
        self.assertEqual(stats["currenthp"], character.getMaxHP())

    def test_power_adding_augment(self):
        character = player("Even Steven", 20, 10, .3, .6, .15)
        powerAddingAugment = augment(
            "Lesser Power Augment of Addition", "power", "add", 5)
        character.addAugment(powerAddingAugment)
        print(character.augments)
        stats = character.returnStats()
        self.assertEqual(stats["power"], 15)

    def test_power_multiplying_augment(self):
        character = enemy("Seven of Heaven", 20, 10, .3, .6, .15)
        powerMultiplyingAugment = augment(
            "Lesser Power Augment of Multiplication", "power", "multiply", 1.2)
        character.addAugment(powerMultiplyingAugment)
        print(character.augments)
        stats = character.returnStats()
        self.assertEqual(stats["power"], 12)


if __name__ == '__main__':
    unittest.main()
