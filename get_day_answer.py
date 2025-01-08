import importlib
import sys
import time

module = sys.argv[1]
folder = sys.argv[2]

day_module = importlib.import_module(module)

start = time.time()
print(day_module.answer(f"{folder}/data"))
end = time.time()

print("Executed in", end - start, "seconds.")
