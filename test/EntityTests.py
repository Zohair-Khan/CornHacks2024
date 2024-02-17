import unittest
from game.classes.entity import entity
from game.classes.player import player
import game.classes.fight
import game.classes.augments
from game.classes.enemy import enemy

class TestEntityMethods(unittest.TestCase):

    def test_init_player_currenthp(self):
        character = player("Even Steven",20,10,.3,.6,.15);
        stats = character.returnStats();
        self.assertEqual(stats["maxhp"], 20);
        self.assertEqual(stats["currenthp"], character.getMaxHP())

if __name__ == '__main__':
    unittest.main()
