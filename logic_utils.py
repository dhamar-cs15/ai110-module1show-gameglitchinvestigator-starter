from typing import Optional


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


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
