import pytest

from logic_utils import (
    check_guess,
    get_attempt_limit_for_difficulty,
    get_range_for_difficulty,
    is_guess_in_range,
    parse_guess,
    update_score,
)


def test_get_range_for_each_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 500)


def test_get_range_rejects_unknown_difficulty():
    with pytest.raises(ValueError, match="Unknown difficulty"):
        get_range_for_difficulty("Extreme")


@pytest.mark.parametrize(
    ("difficulty", "expected_limit"),
    [("Easy", 6), ("Normal", 8), ("Hard", 5)],
)
def test_get_attempt_limit_for_each_difficulty(difficulty, expected_limit):
    assert get_attempt_limit_for_difficulty(difficulty) == expected_limit


def test_get_attempt_limit_rejects_unknown_difficulty():
    with pytest.raises(ValueError, match="Unknown difficulty"):
        get_attempt_limit_for_difficulty("Extreme")


@pytest.mark.parametrize(
    ("guess", "low", "high", "expected"),
    [(1, 1, 20, True), (20, 1, 20, True), (0, 1, 20, False), (21, 1, 20, False)],
)
def test_is_guess_in_range_is_inclusive(guess, low, high, expected):
    assert is_guess_in_range(guess, low, high) is expected


@pytest.mark.parametrize("raw", [None, "", "   "])
def test_parse_guess_requires_input(raw):
    assert parse_guess(raw) == (False, None, "Enter a guess.")


def test_parse_guess_accepts_integer():
    assert parse_guess(" 42 ") == (True, 42, None)


@pytest.mark.parametrize("raw", ["3.9", "3.0", "not a number", "NaN", "inf"])
def test_parse_guess_rejects_non_integer_input(raw):
    assert parse_guess(raw) == (False, None, "Enter a whole number.")


@pytest.mark.parametrize(
    ("guess", "secret", "expected"),
    [
        (50, 50, ("Win", "🎉 Correct!")),
        (60, 50, ("Too High", "📉 Go LOWER!")),
        (40, 50, ("Too Low", "📈 Go HIGHER!")),
        (9, "10", ("Too Low", "📈 Go HIGHER!")),
        (10, "10", ("Win", "🎉 Correct!")),
        (11, "10", ("Too High", "📉 Go LOWER!")),
    ],
)
def test_check_guess_returns_correct_outcome_and_message(guess, secret, expected):
    assert check_guess(guess, secret) == expected


@pytest.mark.parametrize(
    ("attempt_number", "expected_points"),
    [(1, 100), (2, 90), (10, 10), (12, 10)],
)
def test_winning_score_decreases_by_attempt(attempt_number, expected_points):
    assert update_score(0, "Win", attempt_number) == expected_points


@pytest.mark.parametrize("outcome", ["Too High", "Too Low"])
def test_incorrect_guess_reduces_score_by_five(outcome):
    assert update_score(20, outcome, 2) == 15


def test_unknown_outcome_does_not_change_score():
    assert update_score(20, "Invalid", 1) == 20
