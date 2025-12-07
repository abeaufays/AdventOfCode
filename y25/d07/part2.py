from utils import maps
import numpy as np


def answer(filename: str) -> int:
    with open(filename) as file:
        map_data = maps.str_to_map(file.read())

    layer_size = len(map_data[0, :])
    positions_on_layer = [0 if cell != "S" else 1 for cell in map_data[0, :]]
    for current_layer in map_data:
        splitter_indexes = np.where(current_layer == "^")[0]
        positions_on_next_layer = [0] * layer_size
        for position, amount in enumerate(positions_on_layer):
            if np.any(splitter_indexes == position):
                positions_on_next_layer[position - 1] += amount
                positions_on_next_layer[position + 1] += amount
            else:
                positions_on_next_layer[position] += amount
        positions_on_layer = positions_on_next_layer

    return sum(positions_on_layer)
