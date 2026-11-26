# Bug reports for exercise3.py

Line: 3
Problem: The function claims that an empty list has an average of 0, but when the list is empty, `len(numbers)` is 0, which causes division by zero. This will raise a ZeroDivisionError, not return 0 as specified.  
Example: Input: [] → Expected: 0, but actual: ZeroDivisionError  
Fix: `return sum(numbers) / len(numbers) if numbers else 0`

Line: 8
Problem: The function says that if the text is empty, it returns "", but `split()` on an empty string returns an empty list, and `split()[0]` will raise an IndexError.  
Example: Input: "" → Expected: "", but actual: IndexError  
Fix: `return text.split()[0] if text.strip() else ""`

Line: 12
Problem: The function states that if total is 0, the result is 0, but the current code `part / total * 100` will raise a ZeroDivisionError when total is 0.  
Example: Input: part=5, total=0 → Expected: 0, but actual: ZeroDivisionError  
Fix: `return part / total * 100 if total != 0 else 0`
