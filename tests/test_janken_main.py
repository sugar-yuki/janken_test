import unittest
from unittest.mock import patch
import sys
sys.path.append("./source")
from source.janken_main import main

class TestJankenMain(unittest.TestCase):
    @patch('computer.computer_pon', side_effect=['グー', 'チョキ', 'パー'])
    @patch('player.player_pon', side_effect=['パー', 'グー', 'チョキ'])
    def test_main(self, mock_player, mock_computer):
        # 期待される結果:
        # ラウンド1: プレイヤー勝ち (パー vs グー)
        # ラウンド2: プレイヤー勝ち (グー vs チョキ)
        # ラウンド3: コンピュータ勝ち (チョキ vs パー)
        with patch('builtins.print') as mock_print:
            main()
        self.assertEqual(mock_player.call_count, 3)
        self.assertEqual(mock_computer.call_count, 3)
if __name__ == '__main__':
     unittest.main()