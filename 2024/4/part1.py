import numpy as np
import numpy.typing as npt


def answer(input_: str) -> int:
    word_search = _sanitize(input_)
    result = 0

    width = len(word_search[0])  # Assumption that the input is rectangle shaped
    height = len(word_search)

    searched_word = "XMAS"

    def _is_word_valid(word):
        return "".join(word) in {searched_word, searched_word[::-1]}

    for line_idx in range(height):
        for col_idx in range(width):
            # horizontal
            if col_idx < width - len(searched_word) + 1:
                word = word_search[line_idx, col_idx : col_idx + len(searched_word)]
                result += 1 if _is_word_valid(word) else 0
            # vertical
            if line_idx < height - len(searched_word) + 1:
                word = word_search[line_idx : line_idx + len(searched_word), col_idx]
                result += 1 if _is_word_valid(word) else 0
            # diagonal
            if (
                col_idx < width - len(searched_word) + 1
                and line_idx < height - len(searched_word) + 1
            ):
                square = word_search[
                    line_idx : line_idx + len(searched_word),
                    col_idx : col_idx + len(searched_word),
                ]
                word = [square[i, i] for i in range(len(searched_word))]
                result += 1 if _is_word_valid(word) else 0
                word = [
                    square[i, len(searched_word) - i - 1]
                    for i in range(len(searched_word))
                ]
                result += 1 if _is_word_valid(word) else 0

    return result


def _sanitize(inp: str) -> npt.ArrayLike:
    lines = inp.split("\n")
    return np.array([list(line) for line in lines])


if True:
    assert (
        result := (
            answer("""......
......
......
..XMAS""")
        )
    ) == (
        expected := 1
    ), f"Horizontal on the bottom right side: {result} is not {expected}"

    assert (
        result := (
            answer("""......
.....X
.....M
.....A
.....S""")
        )
    ) == (
        expected := 1
    ), f"Vertical on the bottom right side: {result} is not {expected}"

    assert (
        result := (
            answer("""......
..X..X
...MM.
...AA.
..S..S""")
        )
    ) == (
        expected := 2
    ), f"Diagonal on the bottom right side: {result} is not {expected}"


with open("2024/4/test") as file:
    assert (result := answer(file.read())) == (
        expected := 18
    ), f"Test sample: {result} is not {expected}"

with open("2024/4/data") as file:
    print(answer(file.read()))
