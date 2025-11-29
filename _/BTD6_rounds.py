import json, os

for i in os.listdir():
    print(i)
    if ".json" in i:
        f = json.load(open(i, "r", encoding="utf-8"))

        if f["m_Script"]["m_PathID"] != 2874840442446643449: continue
        
        o = []

        print(f["scale"])

        for x in f["rounds"]:
            p = []
            for y in x["bloonGroups"]:
                a = dict()
                a["bloon"] = y["bloon"]
                a["count"] = y["count"]
                a["start"] = round(y["start"],2)
                a["duration"] = round(y["duration"],2)
                p.append(a)
            
            p = sorted(p, key=lambda d: d['start'])

            o.append(p)

        d = {'rounds': o, 'scale': f['scale'], 'incomeSet': 'Rogue'}
        #print(d)

        w = open(f"resorted/{i}", "w", encoding="utf-8")
        json.dump(d, w)

        #break

            
#for i in ["Red", "Blue", "Green", "Yellow", "Pink", "Black", "White", "Purple", "Zebra", "Lead", "Rainbow", "Ceramic"]:
#    print(f'    {i:<20}= "[[File:BTD6 bloon {i}.png|20px|link={i} Bloon (BTD6)]][[{i} Bloon (BTD6)|{i}]]",    {i}Camo       = "[[File:BTD6 bloon {i}Camo.png|20px|link={i} Bloon (BTD6)]][[Camo Bloon (BTD6)|Camo]] [[{i} Bloon (BTD6)|{i}]]",    {i}Regrow     = "[[File:BTD6 bloon {i}Regrow.png|20px|link={i} Bloon (BTD6)]][[Regrow Bloon (BTD6)|Regrow]] [[{i} Bloon (BTD6)|{i}]]",    {i}RegrowCamo = "[[File:BTD6 bloon {i}RegrowCamo.png|20px|link={i} Bloon (BTD6)]][[Camo Bloon (BTD6)|Camo]] [[Regrow Bloon (BTD6)|Regrow]] [[{i} Bloon (BTD6)|{i}]]",')
    
