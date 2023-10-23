import unittest
import os
import json
from dotenv import load_dotenv


load_dotenv()


class TestKeys(unittest.TestCase):
    """This is the test suite"""
    def test_keys(self):
        """It should read valid firebase keys"""

        path_to_keys = os.getenv("FIREBASE_KEYS")
        print(path_to_keys)
        with open(path_to_keys, 'r') as f:
            keys = json.load(f)
        self.assertEqual(keys['client_id'], "111351910762221364858")
