import pytest
from task1 import get_score, INITIAL_STAMP, generate_game, ScoreException

game_stamps = generate_game()

def extract_scores(d: dict):
    return ((d2 := d['score'])['home'], d2['away'])


def test_01():
    assert get_score(None, 1) == extract_scores(INITIAL_STAMP)
    assert get_score(game_stamps, -1) == extract_scores(INITIAL_STAMP)

    d = game_stamps[-1]
    offset = d['offset']
    assert get_score(game_stamps, offset) == extract_scores(d)
    assert get_score(game_stamps, offset + 1) == extract_scores(d)

    i = len(game_stamps) // 2
    d = game_stamps[i]
    offset = d['offset']
    assert get_score(game_stamps, offset) == extract_scores(d)

    with pytest.raises(ScoreException):
        get_score(game_stamps, '05')
    with pytest.raises(ScoreException):
        get_score('list', 5)
    with pytest.raises(ScoreException):
        get_score([{1: 2}], 5)
