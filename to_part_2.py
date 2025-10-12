from pathlib import Path
import sys
import shutil

folder = Path(sys.argv[1])


shutil.copy(folder / "part1.py", folder / "part2.py")
shutil.copy(folder / "test_part1.py", folder / "test_part2.py")

dotted_path = ".".join(str(folder).split("/")[-2:])

with open(folder / "test_part2.py", "r") as file:
    new_content = file.read().replace(dotted_path + ".part1", dotted_path + ".part2")

with open(folder / "test_part2.py", "w") as file:
    file.write(new_content)
