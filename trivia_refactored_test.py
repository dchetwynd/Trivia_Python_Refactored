import unittest
from trivia_refactored import Game

BOB = 0
MIKE = 1

class TriviaTest(unittest.TestCase):
    def testGameWithOnePlayerIsNotPlayable(self):
        game = Game().with_players(["Bob"])
        self.assertFalse(game.is_playable())
    
    def testGameWithTwoPlayersIsPlayable(self):
        game = Game().with_players(["Bob", "Mike"])
        self.assertTrue(game.is_playable())

    def testGameCanCountPlayers(self):
        game = Game().with_players(["Bob", "Mike"])
        self.assertEqual(2, game.how_many_players)

    def testPlayersStartGameOnPlaceZero(self):
        game = Game().with_players(["Bob", "Mike"])
        self.assertEqual(0, game.places[BOB])
        self.assertEqual(0, game.places[MIKE])

    def testPlayersStartGameWithNoGoldCoins(self):
        game = Game().with_players(["Bob", "Mike"])
        self.assertEqual(0, game.purses[BOB])
        self.assertEqual(0, game.purses[MIKE])
    
    def testPlayersStartGameNotInPenaltyBox(self):
        game = Game().with_players(["Bob", "Mike"])
        self.assertFalse(game.in_penalty_box[BOB])
        self.assertFalse(game.in_penalty_box[MIKE])

    def testAnsweringQuestionWrongPutsPlayerInPenaltyBox(self):
        game = Game().with_players(["Bob"])
        game.wrong_answer()
        self.assertTrue(game.in_penalty_box[BOB])

    def testRollingOddNumberWhenInPenaltyBoxRemovesPlayerFromPenaltyBox(self):
        game = Game().with_players(["Bob"])
        game.in_penalty_box[BOB] = True
        game.roll(1)
        self.assertFalse(game.in_penalty_box[BOB])

    def testRollingEvenNumberWhenInPenaltyBoxDoesNotRemovePlayerFromPenaltyBox(self):
        game = Game().with_players(["Bob"])
        game.in_penalty_box[BOB] = True
        game.roll(2)
        self.assertTrue(game.in_penalty_box[BOB])

    def testGameBeginsWithFirstPlayerAdded(self):
        game = Game().with_players(["Bob", "Mike"])
        self.assertEqual(BOB, game.current_player)

    def testRollingWhenNotInPenaltyBoxAdvancesPlayerByRoll(self):
        game = Game().with_players(["Bob"])
        game.in_penalty_box[BOB] = False
        game.roll(6)
        self.assertEqual(6, game.places[BOB])

    def testRollingOddNumberWhenInPenaltyBoxAdvancesPlayerPlacesByRoll(self):
        game = Game().with_players(["Bob"])
        game.in_penalty_box[BOB] = True
        game.roll(3)
        self.assertEqual(3, game.places[BOB])

    def testRollingEvenNumberWhenInPenaltyBoxDoesNotAdvancePlayer(self):
        game = Game().with_players(["Bob"])
        game.in_penalty_box[BOB] = True
        game.roll(4)
        self.assertEqual(0, game.places[BOB])

    def testPlayerPlaceCannotExceedEleven(self):
        game = Game().with_players(["Bob"])
        game.places[BOB] = 8
        game.roll(5)
        self.assertEqual(1, game.places[BOB])

    def testAnsweringQuestionCorrectlyWhenInPenaltyBoxDoesNotEarnGoldCoin(self):
        game = Game().with_players(["Bob"])
        game.in_penalty_box[BOB] = True
        game.correct_answer()
        self.assertEqual(0, game.purses[BOB])

    def testAnsweringQuestionCorrectlyWhenNotInPenaltyBoxEarnsGoldCoin(self):
        game = Game().with_players(["Bob"])
        game.in_penalty_box[BOB] = False
        game.correct_answer()
        self.assertEqual(1, game.purses[BOB])
    
    def testAnsweringQuestionWronglyDoesNotEarnGoldCoin(self):
        game = Game().with_players(["Bob"])
        game.in_penalty_box[BOB] = False
        game.wrong_answer()
        self.assertEqual(0, game.purses[BOB])

    def testPlayerDoesNotWinTheGameByEarningFiveCoins(self):
        game = Game().with_players(["Bob"])
        game.in_penalty_box[BOB] = False
        game.purses[BOB] = 4
        is_game_won = game.correct_answer()
        self.assertFalse(is_game_won)
 
    def testPlayerWinsTheGameByEarningSixCoins(self):
        game = Game().with_players(["Bob"])
        game.in_penalty_box[BOB] = False
        game.purses[BOB] = 5
        is_game_won = game.correct_answer()
        self.assertTrue(is_game_won)

if __name__ == '__main__':
    unittest.main()
