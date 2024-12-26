import importlib
import sys

year, day, part = sys.argv[1:4]
if year.isnumeric() and day.isnumeric() and part in ("1", "2"):
    day_module = importlib.import_module(f"y{year}.d{day}.part{part}")
    print(day_module.answer(f"y{year}/d{day}/data"))
else:
    print("Expect three args: year day part (i.e. 24 02 1)")
