import unittest
from entity import entity
from player import player
from fight import fight
from augments import augment
from enemy import enemy


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
        # print(character.augments);
        stats = character.returnStats()
        self.assertEqual(stats["power"], 15)

    def test_power_multiplying_augment(self):
        character = enemy("Seven of Heaven", 20, 10, .3, .6, .15)
        powerMultiplyingAugment = augment(
            "Lesser Power Augment of Multiplication", "power", "multiply", 1.2)
        character.addAugment(powerMultiplyingAugment)
        # print(character.augments);
        stats = character.returnStats()
        self.assertEqual(stats["power"], 12)


    def test_power_adding_and_multiplying_augment(self):
        character = player("Even Steven",20,10,.3,.6,.15);
        powerAddingAugment = augment("Lesser Power Augment of Addition", "power", "add", 5);
        character.addAugment(powerAddingAugment);
        # print(character.augments);
        powerMultiplyingAugment = augment("Lesser Power Augment of Multiplication", "power", "multiply", 1.2);
        character.addAugment(powerMultiplyingAugment);
        # print(character.augments);
        stats = character.returnStats();
        self.assertEqual(stats["power"],18);

    def test_power_multiplying_and_adding_augment(self):
        character = player("Even Steven",20,10,.3,.6,.15);
        powerMultiplyingAugment = augment("Lesser Power Augment of Multiplication", "power", "multiply", 1.2);
        character.addAugment(powerMultiplyingAugment);
        powerAddingAugment = augment("Lesser Power Augment of Addition", "power", "add", 5);
        character.addAugment(powerAddingAugment);
        # print(character.augments);
        stats = character.returnStats();
        self.assertEqual(stats["power"],17);

    def test_power_subtracting_augment(self):
        character = player("Even Steven",20,10,.3,.6,.15);
        powerSubtractingAugment = augment("Lesser Power Augment of Subtraction", "power", "add", -2)
        character.addAugment(powerSubtractingAugment)
        stats = character.returnStats();
        self.assertEqual(stats["power"],8)

    def test_power_dividing_augment(self):
        character = player("Even Steven",20,10,.3,.6,.15);
        powerDividingAugment = augment("Lesser Power Augment of Division", "power", "multiply", .8)
        character.addAugment(powerDividingAugment)
        stats = character.returnStats();
        self.assertEqual(stats["power"],8)

    def test_modify_hp(self):
        character_1 = player("Even Steven",20,10,.3,.6,.15);
        character_2 = enemy("Evil Eleven",20,10,.3,.6,.15);
        character_3 = enemy("Sick Seven",20,10,.3,.5,.15);
        character_4 = enemy("Notorious Nine", 20,10,.3,.5,.15); 

        character_1.setCurrentHP(16);
        character_1.modifyHP(5); # add 5 to current HP; exceeds max hp
        self.assertEqual(character_1.getCurrentHP(),character_1.getMaxHP());

        character_2.setCurrentHP(4);
        character_2.modifyHP(-5); # subtract 5; falls below 0
        self.assertFalse(character_2.alive); # GameOver() sets alive boolean to false

        character_3.setCurrentHP(11);
        character_3.modifyHP(5); # add 5; falls below max
        self.assertEqual(character_3.getCurrentHP(),16);

        character_4.setCurrentHP(14);
        character_4.modifyHP(-5); # subtract 5; above 0
        self.assertEqual(character_4.getCurrentHP(),9);

    def test_power_adding_and_multiplying_augment(self):
        character = player("Even Steven",20,10,.3,.6,.15);
        powerAddingAugment = augment("Lesser Power Augment of Addition", "power", "add", 5);
        character.addAugment(powerAddingAugment);
        # print(character.augments);
        powerMultiplyingAugment = augment("Lesser Power Augment of Multiplication", "power", "multiply", 1.2);
        character.addAugment(powerMultiplyingAugment);
        # print(character.augments);
        stats = character.returnStats();
        self.assertEqual(stats["power"],18);

    def test_power_multiplying_and_adding_augment(self):
        character = player("Even Steven",20,10,.3,.6,.15);
        powerMultiplyingAugment = augment("Lesser Power Augment of Multiplication", "power", "multiply", 1.2);
        character.addAugment(powerMultiplyingAugment);
        powerAddingAugment = augment("Lesser Power Augment of Addition", "power", "add", 5);
        character.addAugment(powerAddingAugment);
        # print(character.augments);
        stats = character.returnStats();
        self.assertEqual(stats["power"],17);

    def test_power_subtracting_augment(self):
        character = player("Even Steven",20,10,.3,.6,.15);
        powerSubtractingAugment = augment("Lesser Power Augment of Subtraction", "power", "add", -2)
        character.addAugment(powerSubtractingAugment)
        stats = character.returnStats();
        self.assertEqual(stats["power"],8)

    def test_power_dividing_augment(self):
        character = player("Even Steven",20,10,.3,.6,.15);
        powerDividingAugment = augment("Lesser Power Augment of Division", "power", "multiply", .8)
        character.addAugment(powerDividingAugment)
        stats = character.returnStats();
        self.assertEqual(stats["power"],8)

    def test_modify_hp(self):
        character_1 = player("Even Steven",20,10,.3,.6,.15);
        character_2 = enemy("Evil Eleven",20,10,.3,.6,.15);
        character_3 = enemy("Sick Seven",20,10,.3,.5,.15);
        character_4 = enemy("Notorious Nine", 20,10,.3,.5,.15); 

        character_1.setCurrentHP(16);
        character_1.modifyHP(5); # add 5 to current HP; exceeds max hp
        self.assertEqual(character_1.getCurrentHP(),character_1.getMaxHP());

        character_2.setCurrentHP(4);
        character_2.modifyHP(-5); # subtract 5; falls below 0
        self.assertFalse(character_2.alive); # GameOver() sets alive boolean to false

        character_3.setCurrentHP(11);
        character_3.modifyHP(5); # add 5; falls below max
        self.assertEqual(character_3.getCurrentHP(),16);

        character_4.setCurrentHP(14);
        character_4.modifyHP(-5); # subtract 5; above 0
        self.assertEqual(character_4.getCurrentHP(),9);

if __name__ == '__main__':
    unittest.main()
