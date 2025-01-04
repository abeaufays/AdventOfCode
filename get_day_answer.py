import importlib
import sys

module = sys.argv[1]
folder = sys.argv[2]

day_module = importlib.import_module(module)
print(day_module.answer(f"{folder}/data"))
