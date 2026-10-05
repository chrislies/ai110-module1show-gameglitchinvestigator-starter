import pytest

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


# ---------- get_range_for_difficulty ----------

@pytest.mark.parametrize(
    "difficulty, expected",
    [
        ("Easy", (1, 20)),
        ("Normal", (1, 50)),
        ("Hard", (1, 100)),
    ],
)
def test_range_for_known_difficulties(difficulty, expected):
    assert get_range_for_difficulty(difficulty) == expected


@pytest.mark.parametrize("difficulty", ["", "easy", "HARD", "Insane", None])
def test_range_for_unknown_difficulty_defaults_to_hard(difficulty):
    assert get_range_for_difficulty(difficulty) == (1, 100)


# ---------- parse_guess ----------

def test_parse_guess_none():
    assert parse_guess(None) == (False, None, "Enter a guess.")


def test_parse_guess_empty_string():
    assert parse_guess("") == (False, None, "Enter a guess.")


@pytest.mark.parametrize(
    "raw, expected",
    [
        ("42", 42),
        ("0", 0),
        ("-7", -7),
        ("007", 7),
        (" 5 ", 5),       # int() tolerates surrounding whitespace
        ("3.7", 3),       # floats truncate toward zero
        ("-3.7", -3),
        ("5.0", 5),
        ("2.5", 2),
    ],
)
def test_parse_guess_valid(raw, expected):
    assert parse_guess(raw) == (True, expected, None)


@pytest.mark.parametrize("raw", ["abc", "12abc", "1.2.3", ".", " ", "--5", "nan", "inf"])
def test_parse_guess_invalid(raw):
    assert parse_guess(raw) == (False, None, "That is not a number.")


# ---------- check_guess ----------

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_too_high_message_says_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_message_says_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message


def test_check_guess_off_by_one():
    assert check_guess(51, 50)[0] == "Too High"
    assert check_guess(49, 50)[0] == "Too Low"


def test_check_guess_accepts_string_secret():
    assert check_guess(50, "50")[0] == "Win"
    assert check_guess(60, "50")[0] == "Too High"
    assert check_guess(40, "50")[0] == "Too Low"


def test_check_guess_negative_numbers():
    assert check_guess(-5, -5)[0] == "Win"
    assert check_guess(-4, -5)[0] == "Too High"
    assert check_guess(-6, -5)[0] == "Too Low"


# ---------- update_score ----------

@pytest.mark.parametrize(
    "attempt, expected_points",
    [
        (0, 90),   # 100 - 10*1
        (1, 80),
        (3, 60),
        (8, 10),   # 100 - 90 = 10 (boundary)
        (9, 10),   # would be 0, floored to 10
        (20, 10),  # would be negative, floored to 10
    ],
)
def test_update_score_win(attempt, expected_points):
    assert update_score(0, "Win", attempt) == expected_points


def test_update_score_win_adds_to_current_score():
    assert update_score(25, "Win", 0) == 115


def test_update_score_too_high_even_attempt_adds_five():
    assert update_score(10, "Too High", 0) == 15
    assert update_score(10, "Too High", 2) == 15


def test_update_score_too_high_odd_attempt_subtracts_five():
    assert update_score(10, "Too High", 1) == 5
    assert update_score(10, "Too High", 3) == 5


@pytest.mark.parametrize("attempt", [0, 1, 2, 3])
def test_update_score_too_low_always_subtracts_five(attempt):
    assert update_score(10, "Too Low", attempt) == 5


def test_update_score_can_go_negative():
    assert update_score(0, "Too Low", 1) == -5


@pytest.mark.parametrize("outcome", ["", "Invalid", "win", None])
def test_update_score_unknown_outcome_unchanged(outcome):
    assert update_score(42, outcome, 1) == 42
