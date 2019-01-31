from unittest import TestCase, main
from save_prisoner import saveThePrisoner


class Test(TestCase):



    def test_3(self):
        self.assertEqual(saveThePrisoner(5, 10, 1), 5, msg=None)


if __name__ == '__main__':
    main()
