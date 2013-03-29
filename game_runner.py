from trivia_refactored import Game
import sys
import random

class GameRunner(object):
    def __init__(self, seed, players):
        random.seed(seed)
        self.players = players

    def run(self):
        game = Game().with_players(self.players)
        game_won = False
        
        while not game_won:
            game.roll(random.randrange(5) + 1)
            
            if random.randrange(9) == 7:
                game.wrong_answer()
            else:
                game_won = game.correct_answer()
            game.change_player()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        seed = int(sys.argv[1])
    else:
        seed = None
    
    game_runner = GameRunner(seed, ["Chet", "Pat", "Sue"])
    game_runner.run()
