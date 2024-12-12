import unittest
from source.player import player_pon
from unittest.mock import patch
from unittest.mock import MagicMock


class TestPlayerModule(unittest.TestCase):
    @patch('builtins.input',return_value='1')
    def test_pon1(self,mock_input):
        
        result=player_pon()
        self.assertEqual(result,"グー")
    
    @patch('builtins.input',return_value='2')
    def test_pon2(self,mock_input):
        
        result=player_pon()
        self.assertEqual(result,"チョキ")
    
    @patch('builtins.input',return_value='3')
    def test_pon3(self,mock_input):
        
        result=player_pon()
        self.assertEqual(result,"パー")
   
    @patch('builtins.input', side_effect=['0', '4', '3'])
    def test_player_pon_04(self, mock_input):
        player_pon()
        self.assertEqual(mock_input.call_count, 3) # 3回呼び出されていることを確認
    
if __name__=='__main__':
    unittest.main()