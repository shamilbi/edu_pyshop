'''
В примере кода ниже генерируется список фиксаций состояния счета игры в течение матча.
Разработайте функцию get_score(game_stamps, offset), которая вернет счет на момент offset
в списке game_stamps.
Нужно суметь понять суть написанного кода, заметить нюансы,
разработать функцию вписывающуюся стилем в существующий код, желательно адекватной алгоритмической сложности.
'''

from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


def get_score(game_stamps, offset):
    '''
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.
    '''
    def extract_scores(d: dict):
        return ((d2 := d['score'])['home'], d2['away'])

    res = extract_scores(INITIAL_STAMP)
    if not game_stamps or offset < 0:
        return res
    if offset > (d := game_stamps[-1])['offset']:
        return extract_scores(d)
    for d in game_stamps:
        if d['offset'] > offset:
            break
        res = extract_scores(d)
    # return home, away
    return res


if __name__ == '__main__':
    game_stamps = generate_game()
    pprint(game_stamps)
    pprint(get_score(game_stamps, 1))
