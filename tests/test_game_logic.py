import pytest

from logic_utils import check_guess, get_range_for_difficulty, parse_guess


def test_get_range_for_each_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 500)


def test_get_range_rejects_unknown_difficulty():
    with pytest.raises(ValueError, match="Unknown difficulty"):
        get_range_for_difficulty("Extreme")


@pytest.mark.parametrize("raw", [None, "", "   "])
def test_parse_guess_requires_input(raw):
    assert parse_guess(raw) == (False, None, "Enter a guess.")


def test_parse_guess_accepts_integer():
    assert parse_guess(" 42 ") == (True, 42, None)


@pytest.mark.parametrize("raw", ["3.9", "3.0", "not a number", "NaN", "inf"])
def test_parse_guess_rejects_non_integer_input(raw):
    assert parse_guess(raw) == (False, None, "Enter a whole number.")


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"
