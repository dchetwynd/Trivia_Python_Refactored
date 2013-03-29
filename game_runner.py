from trivia_refactored import Game
from random import randrange, seed
import sys

class GameRunner(object):
    def __init__(self, seed, players):
        self.seed = seed
        self.players = players

    def run(self):
        if self.seed is not None:
            seed(self.seed)
        
        game = Game().with_players(self.players)
        game_won = False
        
        while not game_won:
            game.roll(randrange(5) + 1)
            
            if randrange(9) == 7:
                game.wrong_answer()
            else:
                game_won = game.correct_answer()
            game.change_player()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        seed = int(sys.argv[1])
    else:
        seed = None
    
    game_runner = GameRunner(seed, [])
    game_runner.run()
