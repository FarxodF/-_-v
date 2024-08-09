import unittest


class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def __eq__(self, other):
        return self.name == other.name

    def run(self):
        self.distance += self.speed * 10

    def walk(self):
        self.distance += self.speed * 1


class Tournament:
    def __init__(self, distance, runners):
        self.distance = distance
        self.runners = runners

    def start(self):
        results = {}
        finish_times = {}
        for runner in self.runners:
            runner.distance = 0
            time = 0
            while runner.distance < self.distance:
                runner.run()
                time += 1
            finish_times[runner.name] = time
        sorted_runners = sorted(finish_times, key=finish_times.get)
        for i, name in enumerate(sorted_runners):
            results[i + 1] = name
        return results


def frozen_test(is_frozen):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if is_frozen:
                raise unittest.SkipTest('Тесты в этом кейсе заморожены')
            return func(*args, **kwargs)

        return wrapper

    return decorator


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner = Runner("Усэйн", 10)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    @frozen_test(is_frozen)
    def test_run(self):
        self.runner.run()
        self.assertEqual(self.runner.distance, 100)

    @frozen_test(is_frozen)
    def test_walk(self):
        self.runner.walk()
        self.assertEqual(self.runner.distance, 10)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    @frozen_test(is_frozen)
    def test_race_usain_nick(self):
        tournament = Tournament(90, [self.usain, self.nick])
        results = tournament.start()
        self.__class__.all_results[1] = results
        self.assertTrue(results[len(results)] == "Ник")

    @frozen_test(is_frozen)
    def test_race_andrey_nick(self):
        tournament = Tournament(90, [self.andrey, self.nick])
        results = tournament.start()
        self.__class__.all_results[2] = results
        self.assertTrue(results[len(results)] == "Ник")

    @frozen_test(is_frozen)
    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, [self.usain, self.andrey, self.nick])
        results = tournament.start()
        self.__class__.all_results[3] = results
        self.assertTrue(results[len(results)] == "Ник")
