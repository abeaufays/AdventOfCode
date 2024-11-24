with open("day3/data.txt") as f:
    print(
        ("" if bool(file := f.readlines()) else ""),
        sum(
            [
                sum(
                    [
                        int(match.group())
                        for match in __import__("re").finditer(r"\d+", line)
                        if (
                            (
                                start := match.start() - 1
                                if match.start() > 0
                                else match.start()
                            )
                            or True
                        )
                        and (
                            (
                                end := match.end() + 1
                                if match.end() < len(line) - 1
                                else match.end()
                            )
                            or True
                        )
                        and not set(file[y - 1][start:end] if y > 0 else "")
                        | set(line[start:end])
                        | set(file[y + 1][start:end] if y < len(file) - 1 else "")
                        <= set(__import__("string").digits + ".")
                    ]
                )
                for y, line in enumerate(file)
            ]
        ),
    )
