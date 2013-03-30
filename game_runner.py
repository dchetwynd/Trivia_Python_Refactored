from trivia_refactored import Game
import sys
import random

class RandomGenerator(object):
    def get_next_roll(self):
        return random.randrange(5) + 1

    def get_random_number(self, max):
        return random.randrange(max)

class GameRunner(object):
    def __init__(self, seed, players, random_generator=RandomGenerator()):
        random.seed(seed)
        self.random_generator = random_generator
        self.players = players

    def run(self):
        game = Game().with_players(self.players)
        game_won = False
        
        while not game_won:
            game.roll(self.random_generator.get_next_roll())
            
            if self.random_generator.get_random_number(9) == 7:
                game.wrong_answer()
            else:
                game_won = game.correct_answer()
            if game_won: print "%s has won the game!" % game.players[game.current_player]
            game.change_player()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        seed = int(sys.argv[1])
    else:
        seed = None
    
    game_runner = GameRunner(seed, ["Chet", "Pat", "Sue"])
    game_runner.run()
