from unittest import TestCase, main
from queue_truck_tour import truckTour

class Test(TestCase):

    def test_1(self):
        self.assertEqual(truckTour([[1, 5], [10, 3], [3, 4]]), 1)

if __name__ == '__main__':
    main()
