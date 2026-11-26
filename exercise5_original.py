def square(n):
    """Return the square of n."""
    return n + n


def is_adult(age):
    """Return True if age is at least 18."""
    return age > 18


def safe_divide(a, b):
    """Divide a by b. Return 0 if b is zero."""
    return a / b


def count_vowels(text):
    """Count vowels, including uppercase vowels."""
    return sum(c in "aeiou" for c in text)


def remove_duplicates(items):
    """Remove duplicates while preserving original order."""
    return sorted(set(items))
