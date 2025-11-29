import xml.etree.ElementTree as ET
import json
import os
import math

nl = '\n'

en = ET.parse('English.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()

o = open("pywiki_BMCM_tracks.txt", "w", encoding="utf-8")
    
tl = open("tracklist.json", "r", encoding="utf-8")
dtl = json.load(tl)

tr = open("TerrainDefinitionsSpecial.json", "r", encoding="utf-8")
dtr = json.load(tr)

trs = open("TerrainDefinitionsSpecial.json", "r", encoding="utf-8")
dtrs = json.load(trs)

tts = open("TerrainTowers.json", "r", encoding="utf-8")
dtts = json.load(tts)

tds = open("TrackDifficulty.json", "r", encoding="utf-8")
dtds = json.load(tds)

sms = open("SpecialMissions.json", "r", encoding="utf-8")
dsms = json.load(sms)

toweys = {
    "DartMonkey": "Dart Monkey",
    "TackTower": "Tack Shooter",
    "BoomerangThrower": "Boomerang Thrower",
    "IceTower": "Ice Monkey",
    "GlueGunner": "Glue Gunner",
    "MortarTower": "Mortar Monkey",
    "DartlingGun": "Dartling Gun",
    "MonkeyEngineer": "Monkey Engineer",
    "Bloonchipper": "Bloonchipper",
    "MonkeyAce": "Monkey Ace",
    "HeliPilot": "Heli Pilot",
    "MonkeyBuccaneer": "Monkey Buccaneer",
    "MonkeySub": "Monkey Sub",
    "SuperMonkey": "Super Monkey",
    "MonkeyApprentice": "Monkey Apprentice",
    "BananaFarm": "Banana Farm",
    "MonkeyVillage": "Monkey Village",
    "SpikeFactory": "Spike Factory",
    "NinjaMonkey": "Ninja Monkey",
    "SniperMonkey": "Sniper Monkey",
    "BombTower": "Bomb Shooter"
}

#
# PATH LENGTHS
#
maps = dict()
pterrain = dict()

for i in os.listdir("paths"):
    p = open(f"paths/{i}", "r", encoding="utf-8")
    pd = json.load(p)

    paths = []
    paths2 = []

    for k in pd["Nodes"]:
        paths.append(0)
        xl = k["Points"][0][0]
        yl = k["Points"][0][1]
        for m in k["Points"]:
            paths[-1] += math.sqrt(((m[0] - xl) ** 2) + (((m[1] - yl) ** 2)))
            xl = m[0]
            yl = m[1]

    for x in paths: paths2.append(f"{x:0.2f}")

    diffic = -1
    terrain = "??????"

    for x in dtds["Data"]:
        if x["_ID"] == i.replace("level_", "").replace(".path", ""):
            diffic = x["difficulty"]
            if x["mob_terrainType"] == "": terrain = x["mob_terrainSpecial"]
            else: terrain = x["mob_terrainType"]

    mymap = f"""{{{{BMC track info
|id F={i.replace("level_", "").replace("Def.path", "")}
|id M=level_{i.replace("level_", "").replace(".path", "")}

|name   =
|image F=BMCF map {i.replace("level_", "").replace("Def.path", "")}.png
|image M=BMCM thumb_{i.replace(".path", "")}.png

|difficulty={diffic}
|entrances =1
|exits     =1
|junctions =0
|tunnels   =0
|water     =No
|path lengths F=
|path lengths M={','.join(paths2)}
}}}}
{{{{empty}}}}
{{{{clear|right}}}}"""

    if terrain not in pterrain: pterrain[terrain] = mymap
    else: pterrain[terrain] += "\n" + mymap

    p.close()

#
# TERRAIN
#
for i in dtr["Terrains"]:
    if i["_ID"] == "EventMission" or i["_ID"] == "Caves" or i["_ID"] == "ForgottenGarden": continue
    special = []
    favs = []
    rests = []
    diff = 0
    strongest = ""

    for j in dtrs["Terrains"]:
        if j["terrainType"] == i["_ID"]: special.append("[[" + j["name"] + "]]")
    
    for j in dtts["Terrain"]:
        if j["_ID"] == i["_ID"]:
            for a in j["favoured"]:
                favs.append("[[" + toweys[a["name"]] + " (BMC)|" + toweys[a["name"]] + "]]")
            for a in j["disallowed"]:
                rests.append("[[" + toweys[a] + " (BMC)|" + toweys[a] + "]]")


    for j in dsms["Data"]:
        if j["_ID"] == i["_ID"]:
            diff = j["mob_difficulty"]
            strongest = j["mob_strongestBloon"]

    descm = ""

    for aa in en[0]:
        for bb in aa:
            if bb.attrib["id"] == "LOC_SPECIAL_MISSION_" + i["_ID"] + "_DESC": descm = bb.text

    o.write(f"""{{{{-start-}}}}
'''{i["name"]}'''
{{{{BMC special mission info
|id F={i["_ID"]}
|id M={i["_ID"]}

|name         ={i["name"]}
|image F      =
|image M      =
|description F=
|description M={descm}

|cash       ={i["mob_cashFixed"]}
|bloonstones={i["mob_bloonstonesFixed"]}
|xp         ={i["mob_xpFixed"]}

|quantity       ={i["quantityPerMap"]}
|difficulty     ={diff}
|strongest bloon={strongest}
}}}}
'''{i["name"]}''' is a [[Special Mission (BMC)|Special Mission]] in ''[[Bloons Monkey City]]''.

==Track==
{pterrain[i["_ID"]]}

==Strategy==
{{{{strategy needed}}}}

==Navigation==
{{{{BMC special mission nav}}}}
{{{{BMC terrain nav}}}}
{{{{-stop-}}}}
""")


o.close()
tl.close()

