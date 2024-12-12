import unittest
from unittest.mock import patch
from source.janken_judge import judge

class TestJankenJudge(unittest.TestCase):
    
    def test_judge(self):
        patterns = [
            ('グー', 'グー'),
            ('グー', 'チョキ'),
            ('グー', 'パー'),
            ('パー', 'グー'),
            ('パー', 'チョキ'),
            ('パー', 'パー'),
            ('チョキ', 'グー'),
            ('チョキ', 'チョキ'),
            ('チョキ', 'パー')
        ]
        
        for player_hand, computer_hand in patterns:
            with self.subTest(player = player_hand, computer = computer_hand):
                result = judge(computer_hand, player_hand)
                if player_hand == computer_hand:
                    self.assertEqual(result, 'draw')
                elif (player_hand == 'グー' and computer_hand == 'チョキ') or \
                        (player_hand == 'チョキ' and computer_hand == 'パー') or \
                        (player_hand == 'パー' and computer_hand == 'グー'):
                            self.assertEqual(result, 'player_win')
                else:
                    self.assertEqual(result, 'computer_win')

if __name__ == '__main__':
    unittest.main()