import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from lesson_3.common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from lesson_3.client import process_ans, create_presence

class TestClient(unittest.TestCase):

    def test_no_response(self):
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})

    def test_200_ok(self):
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')

    def test_400_ok(self):
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_presence_user_no(self):
        test = create_presence()
        test[USER][ACCOUNT_NAME] = 'Guest1'
        self.assertNotEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_presence_time_no(self):
        test = create_presence()
        test[TIME] = '123'
        self.assertNotEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})