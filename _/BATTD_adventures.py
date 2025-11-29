import os, json

for i in os.listdir():
    if ".json" in i:
        f = open(i, "r", encoding="utf-8")

        fd = json.load(f)

        p = [0, 0, 0, 0]

        for j in fd["adventureChestRewards"]["keys"]:

            if p[j] == 0:
                p[j] = fd["adventureChestRewards"]["values"][j]["randomRewards"]['m_PathID']
            elif p[j] != fd["adventureChestRewards"]["values"][j]["randomRewards"]['m_PathID']:
                print(i)

        print(p)
        f.close()