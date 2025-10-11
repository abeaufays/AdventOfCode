def answer(filename: str) -> int:
    with open(filename) as file:
        data = list(map(int, file.readlines()))
    result = 0
    for i in range(len(data) - 3):
        first = (data[i], data[i + 1], data[i + 2])
        second = (data[i + 1], data[i + 2], data[i + 3])
        if sum(first) < sum(second):
            result += 1

    return result


if __name__ == "__main__":
    print(answer("y21/d01/data"))
