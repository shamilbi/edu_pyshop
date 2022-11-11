import unittest
from task1 import get_score, INITIAL_STAMP, generate_game


def extract_scores(d: dict):
    return ((d2 := d['score'])['home'], d2['away'])


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.game_stamps = generate_game()

    def test_none(self):
        assert get_score(None, 1) == extract_scores(INITIAL_STAMP)

    def test_bad_offset_1(self):
        assert get_score(self.game_stamps, -1) == extract_scores(INITIAL_STAMP)

    def test_bad_offset_2(self):
        d = self.game_stamps[-1]
        offset = d['offset']
        assert get_score(self.game_stamps, offset + 1) == extract_scores(d)

    def test_offset(self):
        d = self.game_stamps[-1]
        offset = d['offset']
        assert get_score(self.game_stamps, offset) == extract_scores(d)

    def test_mid_offset(self):
        i = len(self.game_stamps) // 2
        d = self.game_stamps[i]
        offset = d['offset']
        assert get_score(self.game_stamps, offset) == extract_scores(d)
