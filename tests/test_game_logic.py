from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

# Bug fix 1: swapped hint messages
def test_too_high_message_says_go_lower():
    # When guess is too high, the hint must say Go LOWER, not Go HIGHER
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_message_says_go_higher():
    # When guess is too low, the hint must say Go HIGHER, not Go LOWER
    _, message = check_guess(40, 50)
    assert "HIGHER" in message

# Bug fix 2: secret must stay an integer, not be converted to a string
def test_check_guess_with_integer_secret():
    # String comparison "9" > "50" is True alphabetically but wrong numerically
    # Ensuring secret stays an int means this correctly returns "Too Low"
    outcome, message = check_guess(9, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
