def square(n):
    """Return the square of n."""
    return n * n


def is_adult(age):
    """Return True if age is at least 18."""
    return age >= 18


def safe_divide(a, b):
    """Divide a by b. Return 0 if b is zero."""
    if b == 0:
        return 0
    return a / b


def count_vowels(text):
    """Count vowels, including uppercase vowels."""
    return sum(1 for c in text if c in "aeiouAEIOU")


def remove_duplicates(items):
    """Remove duplicates while preserving original order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
