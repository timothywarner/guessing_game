import unittest
from unittest.mock import patch
from ..src.guessing_game import play_guessing_game  # Updated import path

class TestGuessingGame(unittest.TestCase):
    """🤓 Unit tests for the awesome Number Guessing Game 🤓"""

    # ... (Your test cases go here)
    # ...

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGuessingGame)
    unittest.TextTestRunner(verbosity=2).run(suite)
