import json
import sys

with open(sys.stdin.readline().rstrip(), "r") as rf, open("misery.json", "w") as wf:
    res = {}
    j = json.load(rf)
    i = 1
    for line in sys.stdin.readlines():
        data = list(map(int, line.split("-")))
        action = j[str(len(data))]
        if action == "n":
            data = list(filter(lambda t: t < 1000 and int(str(t)[-1]) == 1, data))
        elif action == "m":
            data = list(filter(lambda t: t % 3 == 0 or t % 7 == 0, data))
        res[str(i)] = data
        i += 1
    json.dump(res, wf, indent=4)
