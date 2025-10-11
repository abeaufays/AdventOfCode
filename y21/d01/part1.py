def answer(filename: str) -> int:
    with open(filename) as file:
        result = 0
        previous_line = int(file.readline())
        for raw_line in file:
            line = int(raw_line)
            if line > previous_line:
                result += 1
            previous_line = line

    return result


if __name__ == "__main__":
    print(answer("y21/d01/data"))
