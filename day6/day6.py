file = open("day6/data.txt", "r")


def get_start_of_packet_marker_index(input: str):
    return get_first_distinct_caracters_sequence_index(input, 4)


def get_start_of_message_marker_index(input: str):
    return get_first_distinct_caracters_sequence_index(input, 14)


def get_first_distinct_caracters_sequence_index(input: str, size: int):
    for i in range(len(input)-size-1):
        if len(set(input[i:i+size])) == size:
            return i+size


assert get_start_of_packet_marker_index(
    "bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
assert get_start_of_packet_marker_index(
    "nppdvjthqldpwncqszvftbrmjlhg") == 6
assert get_start_of_packet_marker_index(
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
assert get_start_of_packet_marker_index(
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

assert get_start_of_message_marker_index(
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
assert get_start_of_message_marker_index("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
assert get_start_of_message_marker_index("nppdvjthqldpwncqszvftbrmjlhg") == 23
assert get_start_of_message_marker_index(
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
assert get_start_of_message_marker_index(
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26


print(get_start_of_message_marker_index(file.readline()))
