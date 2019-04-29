from unittest import TestCase, main
from acm_Team import acmTeam

class Test(TestCase):


    def test_1(self):
        self.assertEquals(acmTeam(['10101', '11100', '11010', '00101']), [5, 2])

if __name__ == '__main__':
    main()
