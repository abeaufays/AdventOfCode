

def item_to_priority(item: str):
    return (ord(item) - ord('A') + 27) if item.isupper() else (ord(item) - ord('a') + 1)


def find_errors_in_rucksack(rucksack: str):
    middle = len(rucksack)//2
    first_compartment, second_compartement = rucksack[:middle], rucksack[middle:]
    return [i for i in first_compartment if i in second_compartement][0]


def find_badge_in_rucksack_group(group: list[str]):
    assert len(group) == 3
    return [j for j in [i for i in group[0] if i in group[1]] if j in group[2]][0]


file = open("day3/data.txt", "r")

lines = file.readlines()

grouped_rucksack = [lines[i:i+3] for i in range(0, len(lines), 3)]

print(sum([item_to_priority(find_badge_in_rucksack_group(group))
      for group in grouped_rucksack]))


# score = sum(item_to_priority(find_errors_in_rucksack(rucksack))
# for rucksack in file.readlines())
