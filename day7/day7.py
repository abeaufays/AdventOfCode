file = open("day7/data.txt", "r")


data = {}
current_folders = []
check = []

for line_number, line in enumerate(file.readlines()):
    match line.split():
        case ["$", "cd", dir]:
            if dir == "/":
                current_folders = []
            elif dir == "..":
                current_folders = current_folders[:-1]
            else:
                current_folders += [
                    f"{current_folders[-1]}/{dir}" if len(current_folders) else dir]
        case ["$", "ls"]:
            check.append(current_folders.copy())
            continue
        case [size, file_name] if size != "$":
            if size == "dir":
                dir_name = f"{current_folders[-1]}/{file_name}" if len(
                    current_folders) != 0 else file_name
                if not dir_name in data:
                    data[dir_name] = 0
                continue
            else:
                for folder in current_folders:
                    data[folder] += int(size)
        case _:
            assert False, f"Couldn't read line : {line}"

print(data)
print("------------")
print(sum([size for dir, size in data.items() if size <= 100000]))
print("------------")

total_space_taken = sum(
    [size for dir, size in data.items() if "/" not in dir]) + 72939 + 236918 + 28586
total_space = 70e6
space_needed = 30e6
current_free_space = (total_space - total_space_taken)


print(min([size for size in data.values() if (
    size + current_free_space) >= space_needed]))
