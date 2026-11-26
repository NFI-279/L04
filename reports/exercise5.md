Line: 3
Problem: The function doubles the number instead of squaring it.
Example: square(5) returns 10, expected 25.
Fix: return n * n

Line: 8
Problem: The function excludes people who are exactly 18.
Example: is_adult(18) returns False, expected True.
Fix: return age >= 18

Line: 13
Problem: Division by zero is not handled.
Example: safe_divide(10, 0) raises ZeroDivisionError, expected 0.
Fix: Return 0 when b is zero.

Line: 18
Problem: Uppercase vowels are ignored.
Example: count_vowels("AEIOU") returns 0, expected 5.
Fix: Include uppercase vowels.

Line: 23
Problem: Sorting changes the original order of elements.
Example: remove_duplicates([3, 1, 3, 2]) returns [1, 2, 3], expected [3, 1, 2].
Fix: Remove duplicates while preserving insertion order.
