import unittest
from tool import validate


class CardTests(unittest.TestCase):
    def test_requires_accountability_fields(self):
        self.assertEqual(validate({"model_name": "x", "evaluation": "bad"}), ["missing:intended_use", "missing:limitations", "missing:contact", "type:evaluation:object"])


if __name__ == "__main__":
    unittest.main()
