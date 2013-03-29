#!/usr/bin/env python
import sys

class Game:
    def __init__(self):
        self.players = []
        self.places = [0] * 6
        self.purses = [0] * 6
        self.in_penalty_box = [0] * 6
        
        self._initialise_questions()
        self.current_player = 0
 
    def _initialise_questions(self):
        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []
        
        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)

    def with_players(self, players):
        for player in players:
            self._add(player)
        return self

    def is_playable(self):
        return self.how_many_players >= 2
    
    def _add(self, player_name):
        self.players.append(player_name)
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False
        
        print player_name + " was added"
        print "They are player number %s" % len(self.players)
        
        return True
    
    @property
    def how_many_players(self):
        return len(self.players)
    
    def roll(self, roll):
        self._report_player_roll(roll)

        if self._player_will_remain_in_penalty_box(roll):
            print "%s is not getting out of the penalty box" % self.players[self.current_player]
            return
        elif self._player_will_escape_from_penalty_box(roll):
            self._release_player_from_penalty_box()

        self._advance_player(roll)
        self._ask_question()

    def _player_will_remain_in_penalty_box(self, roll):
        return self.in_penalty_box[self.current_player] and roll % 2 == 0

    def _player_will_escape_from_penalty_box(self, roll):
        return self.in_penalty_box[self.current_player] and roll % 2 == 1

    def _report_player_roll(self, roll):
        print "%s is the current player" % self.players[self.current_player]
        print "They have rolled a %s" % roll

    def _release_player_from_penalty_box(self):
        self.in_penalty_box[self.current_player] = False
        print "%s is getting out of the penalty box" % self.players[self.current_player]

    def _advance_player(self, roll):
        self.places[self.current_player] = self.places[self.current_player] + roll
        if self.places[self.current_player] > 11:
            self.places[self.current_player] = self.places[self.current_player] - 12
                
        print self.players[self.current_player] + '\'s new location is ' + \
            str(self.places[self.current_player])

    def _ask_question(self):
        print "The category is %s" % self._current_category
        if self._current_category == 'Pop': print self.pop_questions.pop(0)
        if self._current_category == 'Science': print self.science_questions.pop(0)
        if self._current_category == 'Sports': print self.sports_questions.pop(0)
        if self._current_category == 'Rock': print self.rock_questions.pop(0)
    
    @property
    def _current_category(self):
        if self.places[self.current_player] % 4 == 0: return 'Pop'
        elif self.places[self.current_player] % 4 == 1: return 'Science'
        elif self.places[self.current_player] % 4 == 2: return 'Sports'
        else: return 'Rock'

    def correct_answer(self):
        if not self.in_penalty_box[self.current_player]:
            self._player_earns_coin()
 
        return self._did_player_win()
        
    def _player_earns_coin(self):
        print "Answer was correct!!!!"
        self.purses[self.current_player] += 1
        print self.players[self.current_player] + ' now has ' + \
            str(self.purses[self.current_player]) +  ' Gold Coins.'

    def wrong_answer(self):
        print 'Question was incorrectly answered'
        print self.players[self.current_player] + " was sent to the penalty box"
        self.in_penalty_box[self.current_player] = True
    
    def _did_player_win(self):
        return self.purses[self.current_player] == 6

    def change_player(self):
        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
