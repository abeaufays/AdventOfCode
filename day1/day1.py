content = open("day1/data.txt", "r").read()

res = sum(sorted(sum(map(int, x.split("\n")))
                 for x in (content.split("\n\n")))[-3:])

print(res)
