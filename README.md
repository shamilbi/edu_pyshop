## Задание 1. Разработать функцию определения счета в игре

В примере кода ниже генерируется список фиксаций состояния счета игры в течение матча.
Разработайте функцию `get_score`(`game_stamps`, offset), которая вернет счет на момент offset в списке `game_stamps`.
Нужно суметь понять суть написанного кода, заметить нюансы, разработать функцию вписывающуюся стилем в существующий код, желательно адекватной алгоритмической сложности.

```python
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


game_stamps = generate_game()

pprint(game_stamps)
```

Результат: Ссылка на [gist](https://gist.github.com/shamilbi/02839e815459c0bce37601c5ecc252ec) с исходным кодом функции

## Задание 2. Разработать тесты для функции определения счета в игре

Для разработанной в предыдущем задании функции `get_score`(`game_stamps`, offset) разработайте unit-тесты на фреймворке unittest.
Тесты должны учитывать все возможные случаи использования функции, концентрироваться на проверке одного случая,
не повторяться, название тестов должно отражать суть выполняемой проверки.

Результат: Ссылка на [gist](https://gist.github.com/shamilbi/466507a7c281f519998b00952042a976) с исходным кодом тестов
