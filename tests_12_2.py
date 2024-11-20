import runner_2 as runner
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = runner.Runner('Усэйн', 10)
        self.runner2 = runner.Runner('Андрей', 9)
        self.runner3 = runner.Runner('Ник', 3)

    def test1(self):
        dist = runner.Tournament(90, self.runner1, self.runner3)
        self.all_results.update({1: dist.start()})
        self.assertTrue(self.all_results[1][2], 'Ник')

    def test2(self):
        dist = runner.Tournament(90,  self.runner2, self.runner3)
        self.all_results.update({2: dist.start()})
        self.assertTrue(self.all_results[2][2], 'Ник')

    def test3(self):
        dist = runner.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results.update({3: dist.start()})
        self.assertTrue(self.all_results[3][3], 'Ник')

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results[1])
        print(cls.all_results[2])
        print(cls.all_results[3])


if __name__ == '__main__':
    unittest.main()
