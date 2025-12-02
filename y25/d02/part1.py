def answer(filename: str) -> int:
    result = 0
    with open(filename) as file:
        content = file.read()
        ranges = content.split(",")
        for range_ in ranges:
            start, end = range_.split("-")
            if len(start) == len(end) and len(start) % 2 == 1:
                continue

            current = start

            while int(current) <= int(end):
                if len(current) % 2 == 1:
                    current = "1" + ("0" * (len(current)))
                    continue

                first_half, second_half = (
                    current[: len(current) // 2],
                    current[len(current) // 2 :],
                )

                if first_half != second_half:
                    if int(first_half) > int(second_half):
                        current = first_half * 2
                        continue
                    else:
                        current = str(int(first_half) + 1) * 2
                        continue

                result += int(current)

                current = str(int(first_half) + 1) * 2

    return result
