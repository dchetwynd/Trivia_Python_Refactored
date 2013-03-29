import unittest
import os
import sys
from StringIO import StringIO
from game_runner import GameRunner

def run_game_directly(seed):
    os.system("python trivia_original.py %s > original_output.txt" % seed)
    with open("original_output.txt") as trivia_file:
        original_game_output = trivia_file.read()
    return original_game_output

def run_game_with_game_runner(seed, players):
    original_stdout = sys.stdout
    try:
        output = StringIO()
        sys.stdout = output
        game_runner = GameRunner(seed, players)
        game_runner.run()
        game_runner_output = output.getvalue()
    finally:
        sys.stdout = original_stdout
    return game_runner_output

class TriviaTest(unittest.TestCase):
    def testGameRunnerGivesSameOutputAsOriginalScript(self):
        game_runner_output = run_game_with_game_runner(seed=100,
                                players=["Chet", "Pat", "Sue"])
        original_game_output = run_game_directly(seed=100)

        self.assertEqual(original_game_output, game_runner_output)

if __name__ == '__main__':
    unittest.main()
