import unittest
from encoders.jsons import json_restructure

class TestEncoders(unittest.TestCase):
    def test_assert_PLN_in_keys(self):
        result = json_restructure(
            keys = ["cur", "amount"],
            record = {"cur": "PLN", "amount": 100}
        )
        self.assertIn("PLN", result.keys())