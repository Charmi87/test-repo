def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    test_string_1 = "Hello World"
    print(f"Number of vowels in '{test_string_1}': {count_vowels(test_string_1)}")

    test_string_2 = "Python Programming"
    print(f"Number of vowels in '{test_string_2}': {count_vowels(test_string_2)}")

    test_string_3 = "AEIOUaeiou"
    print(f"Number of vowels in '{test_string_3}': {count_vowels(test_string_3)}")

    test_string_4 = "Rhythm"
    print(f"Number of vowels in '{test_string_4}': {count_vowels(test_string_4)}")