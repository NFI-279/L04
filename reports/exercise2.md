# Bug reports for exercise2.py

Line: 13
Problem: The `clamp` function incorrectly uses `max(low, min(x, low))`. It should be `max(low, min(x, high))` to ensure the value is clamped between `low` and `high`, not between `low` and `low`. This causes values above `low` but below `high` to be incorrectly clamped back to `low`.
Example: Input: x=10, low=5, high=15. Expected result: 10. Actual result: 5 (due to error in logic).
Fix: Line 13 should be `return max(low, min(x, high))`
