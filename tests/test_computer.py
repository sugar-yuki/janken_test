import unittest
from unittest.mock import patch
from source.computer import computer_pon

class TestComputer(unittest.TestCase):
    
    @patch("random.choice")
    def test_guu(self, mock_choice):
        mock_choice.return_value = 'グー'
        self.assertEqual(computer_pon(), 'グー')

    @patch("random.choice")
    def test_tyoki(self, mock_choice):
        mock_choice.return_value = 'チョキ'
        self.assertEqual(computer_pon(), 'チョキ')
        
    @patch("random.choice")       
    def test_paa(self, mock_choice):
        mock_choice.return_value = 'パー'
        self.assertEqual(computer_pon(), 'パー')

if __name__ == '__main__':
    unittest.main()