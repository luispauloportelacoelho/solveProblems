from unittest import TestCase, main
from poisonous_plants import poisonousPlants

class Test(TestCase):
    def test_0(self):
        self.assertEqual(poisonousPlants([3, 6, 2, 7, 5]), 2)

    def test_1(self):
        self.assertEqual(poisonousPlants([6, 5, 8, 4, 7, 10, 9]), 2)

    #def test_2(self):
    #    self.assertEqual(poisonousPlants([1, 2, 3, 4, 5]), 1)

    def test_3(self):
        self.assertEqual(poisonousPlants([3, 2, 5, 4]), 2)

    def test_4(self):
        self.assertEqual(poisonousPlants([4, 3, 7, 5, 6, 4, 2]), 3)

if __name__ == '__main__':
    main()
