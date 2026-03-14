# sum_recursion.py

def adding_up_to(numbers, index):
    """
    Recursively sums all numbers in the list up to and including the given index.
    """

    # Defensive checks
    if not numbers:
        return 0

    if index < 0:
        return 0

    if index >= len(numbers):
        raise IndexError("Index is out of range.")

    # Base case
    if index == 0:
        return numbers[0]

    # Recursive case
    return numbers[index] + adding_up_to(numbers, index - 1)


# --- Example Usage ---

print(adding_up_to([1, 4, 5, 3, 12, 16], 4))  # Expected: 25
print(adding_up_to([4, 3, 1, 5], 1))          # Expected: 7
