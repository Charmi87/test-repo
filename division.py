def divide_numbers(num1, num2):
    """
    Calculates the division of two numbers.

    Args:
        num1 (int or float): The dividend.
        num2 (int or float): The divisor.

    Returns:
        float: The result of the division.

    Raises:
        ValueError: If the divisor is zero.
    """
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2
