import unittest
from Army import Army
from Chinese import Chinese
from English import English
from Pikeman import Pikeman
from Archer import Archer
from Knight import Knight

class TestArmySystem(unittest.TestCase):

    def setUp(self):
        self.army_chino = Army(Chinese())
        self.army_ingles = Army(English())

    def test_initial_gold(self):
        self.assertEqual(self.army_chino.gold, 1000)
        self.assertEqual(self.army_ingles.gold, 1000)

    def test_initial_units(self):
        self.assertEqual(len(self.army_chino.unit), 29)  # 2 + 25 + 2
        self.assertEqual(len(self.army_ingles.unit), 30)  # 10 + 10 + 10

    def test_train_pikeman(self):
        pikeman = next((u for u in self.army_ingles.unit if u.type == "Pikeman"), None)
        old_force = pikeman.force
        pikeman.training(self.army_ingles)
        self.assertEqual(pikeman.force, old_force + 3)
        self.assertEqual(self.army_ingles.gold, 990)

    def test_transform_pikeman_to_archer(self):
        pikeman = next((u for u in self.army_chino.unit if u.type == "Pikeman"), None)
        new_unit = pikeman.transform(self.army_chino)
        self.assertEqual(new_unit.type, "Archer")
        self.assertEqual(new_unit.force, pikeman.force)
        self.assertEqual(self.army_chino.gold, 970)

    def test_transform_archer_to_knight(self):
        archer = next((u for u in self.army_chino.unit if u.type == "Archer"), None)
        new_unit = archer.transform(self.army_chino)
        self.assertEqual(new_unit.type, "Knight")
        self.assertEqual(new_unit.force, archer.force)
        self.assertEqual(self.army_chino.gold, 960)

    def test_battle_outcome(self):
        self.army_chino.unit = []  # Forzar derrota
        self.army_ingles.attack(self.army_chino)
        self.assertEqual(self.army_ingles.gold, 1100)
        self.assertEqual(len(self.army_chino.unit), 0)

    def test_battle_tie(self):
        self.army_chino.unit = [Pikeman(), Pikeman()]
        self.army_ingles.unit = [Pikeman(), Pikeman()]
        self.army_chino.attack(self.army_ingles)
        self.assertEqual(len(self.army_chino.unit), 0)
        self.assertEqual(len(self.army_ingles.unit), 0)

if __name__ == '__main__':
    unittest.main()
