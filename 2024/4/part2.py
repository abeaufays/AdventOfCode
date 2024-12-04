import numpy as np
import numpy.typing as npt


def answer(input_: str) -> int:
    word_search = _sanitize(input_)
    result = 0

    width = len(word_search[0])  # Assumption that the input is rectangle shaped
    height = len(word_search)

    searched_word = "MAS"

    for line_idx in range(height):
        for col_idx in range(width):
            if (
                col_idx < width - len(searched_word) + 1
                and line_idx < height - len(searched_word) + 1
            ):
                square = word_search[
                    line_idx : line_idx + len(searched_word),
                    col_idx : col_idx + len(searched_word),
                ]

                w1 = "".join([square[i, i] for i in range(len(searched_word))])
                w2 = "".join(
                    [
                        square[i, len(searched_word) - i - 1]
                        for i in range(len(searched_word))
                    ]
                )

                if (w1 == searched_word or w1 == searched_word[::-1]) and (
                    w1 == w2 or w1 == w2[::-1] or w1[::-1] == w2
                ):
                    result += 1

    return result


def _sanitize(inp: str) -> npt.NDArray:
    lines = inp.split("\n")
    return np.array([list(line) for line in lines])


with open("2024/4/test") as file:
    assert (result := answer(file.read())) == (
        expected := 9
    ), f"Test sample: {result} is not {expected}"

with open("2024/4/data") as file:
    print(answer(file.read()))
