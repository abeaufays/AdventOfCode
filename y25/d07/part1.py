from utils import maps
import numpy as np


def answer(filename: str) -> int:
    with open(filename) as file:
        map_data = maps.str_to_map(file.read())

    positions_on_layer = set(np.where(map_data[0, :] == "S")[0])
    result = 0
    for current_layer in map_data:
        splitter_indexes = np.where(current_layer == "^")
        positions_on_next_layer = set()
        for position in positions_on_layer:
            if np.any(splitter_indexes == position):
                result += 1
                positions_on_next_layer.add(position - 1)
                positions_on_next_layer.add(position + 1)
            else:
                positions_on_next_layer.add(position)
        positions_on_layer = positions_on_next_layer

    return result
