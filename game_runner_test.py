import unittest
import os
import sys
from mock import MagicMock
from StringIO import StringIO
from game_runner import GameRunner, RandomGenerator

def run_game_directly(seed):
    os.system("python trivia_original.py %s > original_output.txt" % seed)
    with open("original_output.txt") as trivia_file:
        original_game_output = trivia_file.read()
    return original_game_output

def run_game_with_game_runner(seed, players, random_generator=RandomGenerator()):
    original_stdout = sys.stdout
    try:
        output = StringIO()
        sys.stdout = output
        game_runner = GameRunner(seed, players, random_generator)
        game_runner.run()
        game_runner_output = output.getvalue()
    finally:
        sys.stdout = original_stdout
    return game_runner_output

CORRECT_ANSWER = 5
WRONG_ANSWER = 7

class TriviaTest(unittest.TestCase):
    def testGameRunnerGivesSameOutputAsOriginalScript(self):
        game_runner_output = run_game_with_game_runner(seed=100,
                                players=["Chet", "Pat", "Sue"])
        original_game_output = run_game_directly(seed=100)

        self.assertEqual(original_game_output, game_runner_output)

    def testFirstPlayerAnsweringSixConsecutiveQuestionsCorrectlyWinsGame(self):
        random_numbers = MagicMock(spec=RandomGenerator)
        random_numbers.get_next_roll = MagicMock(return_value=6)
        random_numbers.get_random_number.side_effect = [CORRECT_ANSWER, WRONG_ANSWER,
                                                        CORRECT_ANSWER, WRONG_ANSWER,
                                                        CORRECT_ANSWER, WRONG_ANSWER,
                                                        CORRECT_ANSWER, WRONG_ANSWER,
                                                        CORRECT_ANSWER, WRONG_ANSWER,
                                                        CORRECT_ANSWER]
        game_output = run_game_with_game_runner(seed=200,
                          players=["Bob", "Mike"],
                          random_generator=random_numbers)
        
        self.assertTrue("Bob has won the game!" in game_output)

    def testSecondPlayerWinsGameWithSixConsecutiveCorrectAnswersWhenFirstPlayerAnswersAllQuestionsWrongly(self):
        random_numbers = MagicMock(spec=RandomGenerator)
        random_numbers.get_next_roll = MagicMock(return_value=6)
        random_numbers.get_random_number.side_effect = [WRONG_ANSWER, CORRECT_ANSWER,
                                                        WRONG_ANSWER, CORRECT_ANSWER,
                                                        WRONG_ANSWER, CORRECT_ANSWER,
                                                        WRONG_ANSWER, CORRECT_ANSWER,
                                                        WRONG_ANSWER, CORRECT_ANSWER,
                                                        WRONG_ANSWER, CORRECT_ANSWER]
        game_output = run_game_with_game_runner(seed=200,
                          players=["Bob", "Mike"],
                          random_generator=random_numbers)
        
        self.assertTrue("Mike has won the game!" in game_output)

if __name__ == '__main__':
    unittest.main()
