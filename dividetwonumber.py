def divide_two_numbers(numerator, denominator):
    if denominator == 0:
        if numerator > 0:
            return float('inf')
        elif numerator < 0:
            return float('-inf')
        else: # numerator is 0, so 0/0
            return float('nan')
    else:
        return numerator / denominator

if __name__ == "__main__":
    print(f"10 / 2 = {divide_two_numbers(10, 2)}")
    print(f"5 / 0 = {divide_two_numbers(5, 0)}")
    print(f"-5 / 0 = {divide_two_numbers(-5, 0)}")
    print(f"0 / 0 = {divide_two_numbers(0, 0)}")
    print(f"0 / 10 = {divide_two_numbers(0, 10)}")