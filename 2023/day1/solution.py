import os

filename = os.path.dirname(os.path.realpath(__file__)) + "/data.txt"

result = 0


digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_calibration_values(line: str) -> int:
    first_digit = None
    for i, letter in enumerate(line):
        if letter.isdigit():
            first_digit = int(letter)
            break
        for digit_str, digit in digits.items():
            if line[i:].startswith(digit_str):
                first_digit = digit
                break
        if first_digit is not None:
            break

    last_digit = None
    for i, letter in enumerate(line[::-1]):
        i = len(line) - i - 1
        if letter.isdigit():
            last_digit = int(letter)
            break
        for digit_str, digit in digits.items():
            if line[i:].startswith(digit_str):
                last_digit = digit
                break
        if last_digit is not None:
            break

    return first_digit * 10 + last_digit


with open(filename, "r") as file:
    for line in file:
        calibration_value = get_calibration_values(line)
        print(line, calibration_value)
        result += calibration_value


print(result)
