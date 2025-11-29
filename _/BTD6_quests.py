import xml.etree.ElementTree as ET
import json
import os

en = ET.parse('../btd6lang/English.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ar = ET.parse('../btd6lang/Arabic.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
zhcn = ET.parse('../btd6lang/ChineseSimplified.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
zhtw = ET.parse('../btd6lang/ChineseTraditional.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
da = ET.parse('../btd6lang/Danish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
de = ET.parse('../btd6lang/German.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
es = ET.parse('../btd6lang/Spanish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
esla = ET.parse('../btd6lang/Spanish (LATAM).xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
fi = ET.parse('../btd6lang/Finnish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
fr = ET.parse('../btd6lang/French.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
it = ET.parse('../btd6lang/Italian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ja = ET.parse('../btd6lang/Japanese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ko = ET.parse('../btd6lang/Korean.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
nl = ET.parse('../btd6lang/Dutch.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
no = ET.parse('../btd6lang/Norwegian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
pl = ET.parse('../btd6lang/Polish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ptbr = ET.parse('../btd6lang/Portuguese (Brazil).xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ru = ET.parse('../btd6lang/Russian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
sv = ET.parse('../btd6lang/Swedish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
th = ET.parse('../btd6lang/Thai.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
tr = ET.parse('../btd6lang/Turkish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()

a = open("pywiki_BTD6_quests.txt", "w", encoding="utf-8")

towerkeys = ["ChosenPrimaryHero", "Quincy", "Gwendolin", "StrikerJones", "ObynGreenfoot", "CaptainChurchill", "Benjamin", "Ezili", "PatFusty",
             "Adora", "AdmiralBrickell", "Etienne", "Sauda", "Psi", "Geraldo", "Corvus", "Rosalia", "Silas",
             "DartMonkey", "BoomerangMonkey", "BombShooter", "TackShooter", "IceMonkey", "GlueGunner", "Desperado",
             "SniperMonkey", "MonkeySub", "MonkeyBuccaneer", "MonkeyAce", "HeliPilot", "MortarMonkey", "DartlingGunner",
             "WizardMonkey", "SuperMonkey", "NinjaMonkey", "Alchemist", "Druid", "Mermonkey",
             "BananaFarm", "SpikeFactory", "MonkeyVillage", "EngineerMonkey", "BeastHandler"]

mapkeys = {
    "#ouch": "#Ouch",
    "AdorasTemple": "Adora's Temple",
    "AlpineRun": "Alpine Run",
    "AncientPortal": "Ancient Portal",
    "AnotherBrick": "Another Brick",
    "Balance": "Balance",
    "Bazaar": "Bazaar",
    "Blons": "Blons",
    "BloodyPuddles": "Bloody Puddles",
    "BloonariusPrime": "Bloonarius Prime",
    "CandyFalls": "Candy Falls",
    "Cargo": "Cargo",
    "Carved": "Carved",
    "CastleRevenge": "Castle Revenge",
    "Chutes": "Chutes",
    "Cornfield": "Cornfield",
    "CoveredGarden": "Covered Garden",
    "Cracked": "Cracked",
    "Cubism": "Cubism",
    "DarkCastle": "Dark Castle",
    "DarkDungeons": "Dark Dungeons",
    "DarkPath": "Dark Path",
    "Downstream": "Downstream",
    "EnchantedGlade": "Enchanted Glade",
    "Encrypted": "Encrypted",
    "EndOfTheRoad": "End Of The Road",
    "Erosion": "Erosion",
    "FiringRange": "Firing Range",
    "FloodedValley": "Flooded Valley",
    "FourCircles": "Four Circles",
    "FrozenOver": "Frozen Over",
    "Geared": "Geared",
    "GlacialTrail": "Glacial Trail",
    "Haunted": "Haunted",
    "Hedge": "Hedge",
    "HighFinance": "High Finance",
    "Infernal": "Infernal",
    "InTheLoop": "In The Loop",
    "KartsNDarts": "KartsNDarts",
    "LastResort": "Last Resort",
    "Logs": "Logs",
    "LostCrevasse": "Lost Crevasse",
    "LotusIsland": "Lotus Island",
    "LuminousCove": "Luminous Cove",
    "Mesa": "Mesa",
    "MiddleOfTheRoad": "Middle of the Road",
    "MidnightMansion": "Midnight Mansion",
    "MoonLanding": "Moon Landing",
    "MuddyPuddles": "Muddy Puddles",
    "OffTheCoast": "Off The Coast",
    "OneTwoTree": "One Two Tree",
    "ParkPath": "Park Path",
    "PatsPond": "Pat's Pond",
    "Peninsula": "Peninsula",
    "Polyphemus": "Polyphemus",
    "ProtectTheYacht": "Protect The Yacht",
    "Quad": "Quad",
    "Quarry": "Quarry",
    "QuietStreet": "Quiet Street",
    "Rake": "Rake",
    "Ravine": "Ravine",
    "Resort": "Resort",
    "Sanctuary": "Sanctuary",
    "Scrapyard": "Scrapyard",
    "Skates": "Skates",
    "SpiceIslands": "Spice Islands",
    "Spillway": "Spillway",
    "SpringSpring": "Spring Spring",
    "Streambed": "Streambed",
    "SulfurSprings": "Sulfur Springs",
    "SunkenColumns": "Sunken Columns",
    "SunsetGulch": "Sunset Gulch",
    "TheCabin": "The Cabin",
    "Tinkerton": "Tinkerton",
    "TownCentre": "Town Center",
    "TreeStump": "Tree Stump",
    "Tutorial": "Monkey Meadow",
    "Underground": "Underground",
    "WaterPark": "Water Park",
    "WinterPark": "Winter Park",
    "Workshop": "Workshop",
    "XFactor": "X Factor"
}

modekeys = {
    "AlternateBloonsRounds": "Alternate Bloons Rounds",
    "Impoppable": "Impoppable",
    "Standard": "Standard",
    "HalfCash": "Half Cash",
    "DoubleMoabHealth": "Double HP MOABs",
    "Reverse": "Reverse",
    "Clicks": "CHIMPS",
    "Deflation": "Deflation"
}

def str2(value):
    if value == None: return ""
    ret = str(value)
    if ret == "True": return "1"
    elif ret == "False": return ""
    return ret

def parsed(dat):
    o = ""
    for k, v in dat.items():
        if k == "map":
            o += "\n|" + k + "=" + mapkeys[v]
        elif k == "mode":
            o += "\n|" + k + "=" + modekeys[v]
        elif type(v) != list and type(v) != dict:
            o += "\n|" + k + "=" + str2(v)

        elif k == "towerList":
            o += "\n|_towers="

            towerids = dict()

            for vv in v["TowerRestrictionsContainer"]["items"]:
                if vv["max"] != 0:
                    o2 = "{{BTD6 tower restrictions"
                    for kkk, vvv in vv.items():
                        o2 += "|" + kkk + "=" + str2(vvv)

                    o2 += "}}"
                    towerids[vv["tower"]] = o2

            for i in towerkeys:
                if i in towerids: o += towerids[i]

        elif k == "startRules":
            o += "\n|lives=" + str2(v["lives"])
            o += "\n|maxLives=" + str2(v["maxLives"])
            o += "\n|startingCash=" + str2(v["cash"])
            o += "\n|startRound=" + str2(v["round"])
            o += "\n|endRound=" + str2(v["endRound"])
            o += "\n|revives=" + str2(v["revives"])


            
        elif k == "bloonModifiers":
            o += "\n|speedMultiplier=" + str2(v["speedMultiplier"])
            o += "\n|moabSpeedMultiplier=" + str2(v["moabSpeedMultiplier"])
            o += "\n|bossSpeedMultiplier=" + str2(v["bossSpeedMultiplier"])
            o += "\n|regrowRateMultiplier=" + str2(v["regrowRateMultiplier"])
            o += "\n|bloonHealthMultiplier=" + str2(v["healthMultipliers"]["bloons"])
            o += "\n|moabHealthMultiplier=" + str2(v["healthMultipliers"]["moabs"])
            o += "\n|bossHealthMultiplier=" + str2(v["healthMultipliers"]["boss"])

        elif k == "roundSets":
            if v != []: o += "\n|customRounds=" + ", ".join(v)
            else: o += "\n|customRounds="


    return o

for i in os.listdir("all"):
    f = open(f"all/{i}", "r", encoding="utf-8")
    d = json.load(f)

    if d["m_Script"]["m_PathID"] != 6464275011401217040:
        if d["m_Script"]["m_PathID"] == -7325738532115065713:
            d2 = d

            def n(lang):
                for i in lang[0]:
                    for j in i:
                        if j.attrib['id'] == d["title"] or j.attrib['id'] == (d['subTitle'].replace('Description', 'Name')): return j.text

            def b(lang):
                for i in lang[0]:
                    for j in i:
                        if j.attrib['id'] == d["subTitle"]: return j.text

            if n(en) == None: continue

            print(d['m_Name'])
            a.write(f"""=={n(en)}==
{{{{empty}}}}

===Challenge rules===
""")
            a.write(f"""{{{{BTD6 challenge rules/new
|type=Quest
|description={b(en)}
|victory={v(en)}""")
            
            a.write(parsed(d2["challengeData"]))
            a.write(f"""
}}}}

===In other languages===
{{{{BTD6 last updated|51.0|section=y}}}}
{{{{langlist
|table=btd6_text
|key={d2['title']}
|label=Name
|collapsed=y
|ar   ={n(ar)}
|da   ={n(da)}
|de   ={n(de)}
|es   ={n(es)}
|es-la={n(esla)}
|fi   ={n(fi)}
|fr   ={n(fr)}
|it   ={n(it)}
|ja   ={n(ja)}
|ko   ={n(ko)}
|nl   ={n(nl)}
|no   ={n(no)}
|pl   ={n(pl)}
|pt-br={n(ptbr)}
|ru   ={n(ru)}
|sv   ={n(sv)}
|th   ={n(th)}
|tr   ={n(tr)}
|zh-cn={n(zhcn)}
|zh-tw={n(zhtw)}
}}}}
{{{{langlist
|table=btd6_text
|key={d2['subTitle']}
|label=Description
|collapsed=y
|ar   ={b(ar)}
|da   ={b(da)}
|de   ={b(de)}
|es   ={b(es)}
|es-la={b(esla)}
|fi   ={b(fi)}
|fr   ={b(fr)}
|it   ={b(it)}
|ja   ={b(ja)}
|ko   ={b(ko)}
|nl   ={b(nl)}
|no   ={b(no)}
|pl   ={b(pl)}
|pt-br={b(ptbr)}
|ru   ={b(ru)}
|sv   ={b(sv)}
|th   ={b(th)}
|tr   ={b(tr)}
|zh-cn={b(zhcn)}
|zh-tw={b(zhtw)}
}}}}
{{{{langlist
|table=btd6_text
|key={d['victoryScreenLoc']}
|label=Victory text
|collapsed=y
|ar   ={v(ar)}
|da   ={v(da)}
|de   ={v(de)}
|es   ={v(es)}
|es-la={v(esla)}
|fi   ={v(fi)}
|fr   ={v(fr)}
|it   ={v(it)}
|ja   ={v(ja)}
|ko   ={v(ko)}
|nl   ={v(nl)}
|no   ={v(no)}
|pl   ={v(pl)}
|pt-br={v(ptbr)}
|ru   ={v(ru)}
|sv   ={v(sv)}
|th   ={v(th)}
|tr   ={v(tr)}
|zh-cn={v(zhcn)}
|zh-tw={v(zhtw)}
}}}}
""")
        f.close()
        continue

    def n(lang):
        for i in lang[0]:
            for j in i:
                if j.attrib['id'] == d["questTitleLoc"]: return j.text

    def b(lang):
        for i in lang[0]:
            for j in i:
                if j.attrib['id'] == d["descriptionShortLoc"]: return j.text

    def dd(lang):
        for i in lang[0]:
            for j in i:
                if j.attrib['id'] == d["descriptionLongLoc"]: return j.text

    def v(lang):
        for i in lang[0]:
            for j in i:
                if j.attrib['id'] == d["victoryScreenLoc"]: return j.text
    
    if d["questCategory"] == 9:
        print("aaa")
    else:


        #f2 = open(f"data/Tale{i[:-5]}_0.json", "r", encoding="utf-8") if f"Tale{i[:-5]}_0.json" in os.listdir("data") else open(f"data/{i[:-5]}_0.json", "r", encoding="utf-8") if f"{i[:-5]}_0.json" in os.listdir("data") else open(f"data/{i[:-5]}Quest_0.json", "r", encoding="utf-8")
        #d2 = json.load(f2)
        a.write(f'''{{{{-start-}}}}
\'\'\'{n(en)}\'\'\'
{{{{stub}}}}
{{{{BTD6 quest info
|id={d["id"]}

|name       ={n(en)}
|image      =
|description={b(en)}

|category    ={"Tales" if d["questCategory"] == 0 else "Challenges" if d["questCategory"] == 1 else "Tutorials" if d["questCategory"] == 2 else "Experiments"}
|unlock level={d["unlockLevel"]}
|rewards     =
|introduced  =51.0
|introduced C=
}}}}
\'\'\'{n(en)}\'\'\' is a{'n' if d["questCategory"] == 3 else ''} [[Quest (BTD6)|{"Tale Quest" if d["questCategory"] == 0 else "Challenge Quest" if d["questCategory"] == 1 else "Tutorial Quest" if d["questCategory"] == 2 else "Experiment Quest"}]] in ''[[Bloons TD 6]]''.

==In other languages==
{{{{BTD6 last updated|50.2|section=y}}}}
{{{{langlist
|table=btd6_text
|key={d['questTitleLoc']}
|label=Name
|collapsed=y
|ar   ={n(ar)}
|da   ={n(da)}
|de   ={n(de)}
|es   ={n(es)}
|es-la={n(esla)}
|fi   ={n(fi)}
|fr   ={n(fr)}
|it   ={n(it)}
|ja   ={n(ja)}
|ko   ={n(ko)}
|nl   ={n(nl)}
|no   ={n(no)}
|pl   ={n(pl)}
|pt-br={n(ptbr)}
|ru   ={n(ru)}
|sv   ={n(sv)}
|th   ={n(th)}
|tr   ={n(tr)}
|zh-cn={n(zhcn)}
|zh-tw={n(zhtw)}
}}}}
{{{{langlist
|table=btd6_text
|key={d['descriptionShortLoc']}
|label=Description
|collapsed=y
|ar   ={b(ar)}
|da   ={b(da)}
|de   ={b(de)}
|es   ={b(es)}
|es-la={b(esla)}
|fi   ={b(fi)}
|fr   ={b(fr)}
|it   ={b(it)}
|ja   ={b(ja)}
|ko   ={b(ko)}
|nl   ={b(nl)}
|no   ={b(no)}
|pl   ={b(pl)}
|pt-br={b(ptbr)}
|ru   ={b(ru)}
|sv   ={b(sv)}
|th   ={b(th)}
|tr   ={b(tr)}
|zh-cn={b(zhcn)}
|zh-tw={b(zhtw)}
}}}}

==Navigation==
{{{{BTD6 quest nav}}}}
{{{{-stop-}}}}
''')
    f.close()


a.close()