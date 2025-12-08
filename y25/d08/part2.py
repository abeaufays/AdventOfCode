import math
from sortedcontainers import SortedDict

type vec3d = tuple[int, int, int]


def answer(filename: str) -> int:
    junctions_boxes: list[vec3d] = []
    with open(filename) as file:
        for line in file:
            coords = tuple(map(int, line.split(",")))
            junctions_boxes.append((coords[0], coords[1], coords[2]))

    distances: SortedDict[float, tuple[vec3d, vec3d]] = SortedDict()

    for index, junction_box in enumerate(junctions_boxes[:-1]):
        for other_junction_box in junctions_boxes[index + 1 :]:
            distance = math.dist(junction_box, other_junction_box)
            distances[distance] = (junction_box, other_junction_box)

    clusters: list[set[vec3d]] = []
    while True:
        distance, linked_junctions_boxes = distances.popitem(index=0)
        found_clusters = []
        for cluster in clusters:
            if any(
                linked_junctions_box in cluster
                for linked_junctions_box in linked_junctions_boxes
            ):
                found_clusters.append(cluster)
        if not found_clusters:
            clusters.append({*linked_junctions_boxes})
        elif len(found_clusters) == 1:
            found_clusters.pop().update(linked_junctions_boxes)
        else:
            new_cluster = set()
            for found_cluster in found_clusters:
                clusters.remove(found_cluster)
                new_cluster.update(found_cluster)
            clusters.append(new_cluster)

        if len(clusters) == 1:
            cluster = clusters[0]
            if len(cluster) == len(junctions_boxes):
                break

    return linked_junctions_boxes[0][0] * linked_junctions_boxes[1][0]
