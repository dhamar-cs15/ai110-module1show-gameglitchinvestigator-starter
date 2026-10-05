from typing import Optional, Tuple, Union

# Fix: updated the ranges for each difficulty using agent mode
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    ranges = {
        "Easy": (1, 20),
        "Normal": (1, 100),
        "Hard": (1, 500),
    }
    try:
        return ranges[difficulty]
    except KeyError:
        raise ValueError(f"Unknown difficulty: {difficulty}") from None


def get_attempt_limit_for_difficulty(difficulty: str) -> int:
    """Return the number of allowed guesses for a difficulty."""
    attempt_limits = {
        "Easy": 6,
        "Normal": 8,
        "Hard": 5,
    }
    try:
        return attempt_limits[difficulty]
    except KeyError:
        raise ValueError(f"Unknown difficulty: {difficulty}") from None


def is_guess_in_range(guess: int, low: int, high: int) -> bool:
    """Return whether guess is within the inclusive bounds."""
    return low <= guess <= high


# FIX: Restricted the different possibilities of what the program takes in as user input
def parse_guess(raw: Optional[str]):
    """
    Parse user input into an integer guess without truncating decimal input.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or not raw.strip():
        return False, None, "Enter a guess."

    try:
        value = int(raw)
    except ValueError:
        return False, None, "Enter a whole number."

    return True, value, None

# Fix: Made logic more concise to cover cases where input is too high or too low - using agent mode
def check_guess(guess: int, secret: Union[int, str]) -> Tuple[str, str]:
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    secret_value = int(secret)

    if guess == secret_value:
        return "Win", "🎉 Correct!"
    if guess > secret_value:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = max(10, 100 - 10 * (attempt_number - 1))
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
