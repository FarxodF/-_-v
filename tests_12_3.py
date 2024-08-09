import unittest
from suite_12_3 import RunnerTest, TournamentTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RunnerTest))
    suite.addTest(unittest.makeSuite(TournamentTest))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
