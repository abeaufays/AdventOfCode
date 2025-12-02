def answer(filename: str) -> int:
    result = 0
    with open(filename) as file:
        content = file.read()
        ranges = content.split(",")
        for range_ in ranges:
            start, end = range_.split("-")

            current = start
            while int(current) <= int(end):
                for n in [2, 3, 5, 7]:
                    if len(current) % n == 0:
                        parts = split_in_even_parts(current, len(current) // n)
                        if all(parts[0] == x for x in parts):
                            result += int(current)
                            break
                else:
                    pass  # valid id

                current = str(int(current) + 1)
    return result


def split_in_even_parts(s: str, size: int) -> list[str]:
    return list(map("".join, zip(*[iter(s)] * size)))
