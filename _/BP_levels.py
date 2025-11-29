import json, os

levs = [
    
]

blones = set()

for i in os.listdir("patt"):
    f = open(f"patt/{i}", "r", encoding="utf-8")
    js = json.load(f)
    lev = {
        "bloons": {},
        "obstacles": {},
        "levelModifiers": []
    }

    for j in js["bloons"]:
        if j["data"] not in lev["bloons"]: lev["bloons"][j["data"]] = 0
        lev["bloons"][j["data"]] += 1
        if j['data'] not in blones and j['data'] not in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 138, 261, 264, 267, 268, 269, 270, 516, 523, 524, 525, 526, 582, 587, 588, 589, 590, 774, 775, 777, 778, 779, 1041, 3089, 9233, 10257, 11281, 12305, 13329]: print (j['data'], "-", i[22:-5])
        blones.add(j["data"])

    #lev["bloons"].sort()

    for j in js["obstacles"]:
        if j["type"] not in lev["obstacles"]: lev["obstacles"][j["type"]] = 0
        lev["obstacles"][j["type"]] += 1

    #if lev["victoryConditions"] != [0] or lev["victoryBloonTypes"] != [0] or lev["victoryCounts"] != [0] or lev["numberOfAttempts"] != [0] or lev["bloonScale"] != [0] or lev["allowedMonkeys"] != [0]:
    #    print(i, lev["victoryConditions"], lev["victoryBloonTypes"], lev["victoryCounts"], lev["numberOfAttempts"], lev["bloonScale"], lev["allowedMonkeys"])

    lev["levelModifiers"] = js["levelModifiers"]

    levs.append(lev)

    f.close()

o = open("levs.json", "w", encoding="utf-8")
o.write(json.dumps({"data": levs}))

o.close()
print(blones)