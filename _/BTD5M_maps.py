import xml.etree.ElementTree as ET
import json
import os
import math

nl = '\n'

en = ET.parse('English.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ar = ET.parse('Arabic.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
da = ET.parse('Danish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
de = ET.parse('German.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
es = ET.parse('Spanish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
fi = ET.parse('Finnish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
fr = ET.parse('French.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
it = ET.parse('Italian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ja = ET.parse('Japanese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ko = ET.parse('Korean.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
no = ET.parse('Norwegian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ptbr = ET.parse('BrazilianPortuguese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ru = ET.parse('Russian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
sv = ET.parse('Swedish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
tr = ET.parse('Turkish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()

o = open("pywiki_BTD5M_maps.txt", "w", encoding="utf-8")
    
tl = open("tracklist.json", "r", encoding="utf-8")
ctl = open("coop_tracklist.json", "r", encoding="utf-8")
btl = open("ctracklist.json", "r", encoding="utf-8")

dtl = json.load(tl)
dctl = json.load(ctl)
dbtl = json.load(btl)

fids = []
fnames = []

lengths = {
"bobsleigh_run":               [1947.59437056339],
"dancefloor":                  [2005.125610535344],
"nazca_lines":                 [1547.4858965510678, 1529.3046882021476],
"toyland":                     [1630.2137928966529],
"daffodils":                   [1406.1270201781854],
"carpark":                     [1465.2208443032566],
"snowman":                     [2090.6537889210153],
"oasis":                       [1862.9468054890651],
"bloom":                       [1589.5222892346046],
"checkers":                    [1882.2312569686421],
"roswell":                     [1658.0586195466526],
"throne_room":                 [942.0038829213878, 935.9801792069093],
"lonely_heart":                [1958.168806659133],
"autumn_leaves":               [1581.9611163063676],
"forgotten_garden":            [190.01052602421794, 496.0040649734797, 1751.067348281718],
"head_in_the_clouds":          [1387.5716683321727],
"flooded_lane":                [500.01529921313437, 74.00675644831355, 916.7878024987824, 76.00657866263946, 119.14070317818513],
"walk_in_the_park":            [801.1211904274501, 927.9848968882044],
"ancient_tomb":                [1059.837877294231, 1071.8618003958886],
"wattle_trees":                [1663.7655329424986],
"workshop":                    [862.3488512430414, 860.2401728598185],
"bloon_of_clubs":              [1188.2106006771296],
"villageshore":                [1388.504179302676],
"egg_hunt":                    [997.4544750605231, 878.0789670532338],
"day_of_the_undead":           [961.6660218453643],
"promontory":                  [1089.0174392622732, 0.0],
"tidal_pools":                 [1077.2713340520222],
"bigfoot":                     [687.7254564314334, 659.0212520219685],
"igloos":                      [833.0227667170849, 1056.2667863324716],
"long_range":                  [860.4273224440907],
"challenger_deep":             [1195.0514092977983],
"u_turn":                      [1031.4718957436255, 971.5204604597359],
"one_direction":               [234.9537428652686, 377.7737418085063, 471.05838279347074, 311.24763757996215],
"siege":                       [484.52335350202515, 488.38213750856926, 482.0661412382563, 492.5110355030405],
"tributaries":                 [518.2516214902479, 462.0940264008106, 439.84944376100725, 456.1495397591989, 522.77133621811],
"double_double_crossover":     [37.013511046643494, 593.3114213857705, 49.0, 497.3946645435452, 64.00781202322104, 593.3114213857705, 37.013511046643494, 63.00793600809346, 497.3946645435452, 48.0],
"benguela":                    [430.93866577323405, 439.9231624956331, 569.5243831597569],
"web":                         [1315.1880930494904],
"forestpath":                  [428.12317296519325, 232.28370318145082, 480.91891234231383],
"campfire":                    [472.9685493749056, 400.82695728945157, 402.63754458384255],
"toxic_waste":                 [483.8347087844669, 483.97982201686267, 484.51701205884495, 491.96490812366324],
"river_logging":[1418.51]
}
lengths2 = {
"bobsleigh_run":               [1947.59437056339],
"dancefloor":                  [2005.125610535344],
"nazca_lines":                 [1547.4858965510678, 1529.3046882021476],
"toyland":                     [1630.2137928966529],
"daffodils":                   [1406.1270201781854],
"carpark":                     [1465.2208443032566],
"snowman":                     [2090.6537889210153],
"oasis":                       [1862.9468054890651],
"bloom":                       [1589.5222892346046],
"checkers":                    [1882.2312569686421],
"roswell":                     [1658.0586195466526],
"throne_room":                 [942.0038829213878, 935.9801792069093],
"lonely_heart":                [1958.168806659133],
"autumn_leaves":               [1581.9611163063676],
"forgotten_garden":            [2437.08193927941564],
"head_in_the_clouds":          [1387.5716683321727],
"flooded_lane":                [1685.9571400010548],
"walk_in_the_park":            [801.1211904274501, 927.9848968882044],
"ancient_tomb":                [1059.837877294231, 1071.8618003958886],
"wattle_trees":                [1663.7655329424986],
"workshop":                    [862.3488512430414, 860.2401728598185],
"bloon_of_clubs":              [1188.2106006771296],
"villageshore":                [1388.504179302676],
"egg_hunt":                    [997.4544750605231, 878.0789670532338],
"day_of_the_undead":           [961.6660218453643],
"promontory":                  [1089.0174392622732],
"tidal_pools":                 [1077.2713340520222],
"bigfoot":                     [687.7254564314334, 659.0212520219685],
"igloos":                      [833.0227667170849, 1056.2667863324716],
"long_range":                  [860.4273224440907],
"challenger_deep":             [1195.0514092977983],
"u_turn":                      [1031.4718957436255, 971.5204604597359],
"one_direction":               [1395.0335050472079],
"siege":                       [484.52335350202515, 488.38213750856926, 482.0661412382563, 492.5110355030405],
"tributaries":                 [518.2516214902479, 462.0940264008106, 439.84944376100725, 456.1495397591989, 522.77133621811],
"double_double_crossover":     [630.324932432413994, 610.40247656676624, 630.324932432413994, 608.40260055163866],
"benguela":                    [430.93866577323405, 439.9231624956331, 569.5243831597569],
"web":                         [1315.1880930494904],
"forestpath":                  [660.4068761466441, 480.91891234231383],
"campfire":                    [472.9685493749056, 400.82695728945157, 402.63754458384255],
"toxic_waste":                 [483.8347087844669, 483.97982201686267, 484.51701205884495, 491.96490812366324],
"mosaic": [1808.3208961730693],
"fast_track": [1869.4044794289275]
}

namess = {
"monkey_lane":                 "Monkey Lane",
"bobsleigh_run":               "Bobsleigh Run",
"dancefloor":                  "Dance Floor",
"nazca_lines":                 "Nazca Lines",
"toyland":                     "Toyland",
"daffodils":                   "Daffodils",
"carpark":                     "Parking Lot",
"snowman":                     "Snowman",
"oasis":                       "Oasis",
"bloom":                       "Bloom",
"present_delivery":            "Present Delivery",
"rabbit_holes":                "Rabbit Holes",
"snowy_backyard":              "Snowy Backyard",
"sprint_track":                "Sprint Track",
"express_shipping":            "Express Shipping",
"checkers":                    "Checkers",
"skull_peak":                  "Skull Peak",
"lobby":                       "Lobby",
"3_times_around":              "3 Times Around",
"grotto":                      "North Pole",
"patch":                       "Patch",
"hedge_maze":                  "Maze",
"fireworks":                   "Fireworks",
"brick_wall":                  "Brick Wall",
"z_factor":                    "Z Factor",
"maze":                        "Park Path",
"frozen_lake":                 "The Rink",
"roswell":                     "Roswell",
"space_truckin":               "Space Truckin",
"throne_room":                 "Over-Throne",
"lonely_heart":                "Lonely Heart",
"autumn_leaves":               "Autumn Leaves",
"forgotten_garden":            "Forgotten Garden",
"head_in_the_clouds":          "Head In The Clouds",
"flooded_lane":                "Flooded Lane",
"walk_in_the_park":            "Walk In The Park",
"ancient_tomb":                "Ancient Tomb",
"hearthside":                  "Hearthside",
"six_feet":                    "Six Feet",
"river_rapids":                "River Rapids",
"wattle_trees":                "Wattle Trees",
"pyramids":                    "Pyramids",
"dune_sea":                    "Dune Sea",
"lava_fields":                 "Lava Fields",
"ice_flow":                    "Ice Flow",
"country_road":                "Country Road",
"jungle":                      "Jungle",
"workshop":                    "Workshop",
"bloon_of_clubs":              "Bloon Of Clubs",
"archipelago":                 "Archipelago",
"crop_circles":                "Bloon Circles",
"slalom":                      "Slalom",
"stream":                      "Snake River",
"dock_side":                   "Dockside",
"villageshore":                "Village Shore",
"trick_or_treat":              "Trick Or Treat",
"egg_hunt":                    "Egg Hunt",
"day_of_the_undead":           "Day of the Undead",
"promontory":                  "Land's End",
"tidal_pools":                 "Tidal Pools",
"bigfoot":                     "Bigfoot",
"igloos":                      "Igloos",
"battle_knot":                 "Battle Knot",
"candyland":                   "Candyland",
"crypt_keeper":                "Crypt Keeper",
"long_range":                  "Long Range",
"water_hazard":                "Water Hazard",
"rink_revenge":                "Rink Revenge",
"challenger_deep":             "Challenger Deep",
"scorched_earth":              "Scorched Earth",
"u_turn":                      "U-Turn",
"the_great_divide":            "The Great Divide",
"the_eye":                     "The Eye",
"one_direction":               "Phase Portals",
"lightning_scar":              "Lightning Scar",
"go_with_the_flow":            "Switch",
"mount_magma":                 "Mount Magma",
"siege":                       "Siege",
"tributaries":                 "Tributaries",
"double_double_crossover":     "Double Double Cross",
"tunnels":                     "Tunnels",
"castle":                      "Castle",
"against_the_clock":           "Clock",
"drag_strip":                  "Drag Strip",
"canyon":                      "Death Valley",
"treetops":                    "Treetop",
"runway":                      "Runway",
"down_the_drain":              "Down The Drain",
"benguela":                    "Benguela",
"web":                         "Web",
"forestpath":                  "Forest Path",
"campfire":                    "Campfire",
"toxic_waste":                 "Toxic Waste",
"tar_pit":                     "Tar Pits",
"main_street":                 "Main Street",
"radioactive":                 "Bloontonium Lab",
"mosaic": "Mosaic",
"fast_track": "Fast Track",
"alpine_lake": "Alpine Lake",
"dollar": "Cash Money",
"dark_dungeon": "Dark Dungeon",
"south_coast": "South Coast",
"unfairshare": "Unfair Share",
"haunted_swamp": "Haunted Swamp",
"spidermap": "Spider Map",
"no_escape": "No Escape",
"monkey_town": "Protect Monkey Town",
"the_crucible": "The Crucible",
"bloonvasion":"Bloonvasion",
"river_logging":"River Logging",
"sandstorm": "Sandstorm"
}

for i in os.listdir("levelDefs"):
    ac = open(f"levelDefs/{i}", "r")
    act = ac.read()
    fid = ''
    fname = ''



    start = act.find('id = "') + 6
    j = start
    while act[j] != '"':
        fid += act[j]
        j += 1

    start = act.find('name = "') + 8
    j = start
    while act[j] != '"':
        fname += act[j]
        j += 1

    fids.append(fid)
    fnames.append(fname)

    ac.close()

for j in os.listdir("LevelDefinitions_c"):
    for k in os.listdir("LevelDefinitions"):
        if k == j:
            m = open(f"LevelDefinitions/{j}/{j}.path", "r", encoding="ANSI")
            c = open(f"LevelDefinitions_c/{j}/{j}.path", "r", encoding="ANSI")

            md = m.read()
            cd = c.read()

            if md != cd and 'DGDATA' not in md: print(j, "X")
            m.close()
            c.close()

    

for i in dtl["Tracks"]:

    coop = 0

    for j in dctl["Tracks"]:
        if i[1] == j[1]:
            coop = 1
            break

    water = i[5]

    c = 0

    for j in dbtl["Tracks"]:
        if i[1] == j[1]:
            c = 1
            break

    f = 0
    fname = ''
    fid = ''

    for j in range(len(fnames)):
        if namess[i[1]].lower() == fnames[j].lower():
            f = 1
            fid = fids[j]
            fname = fnames[j]

    if i[1] in ['sandstorm']:

        totallength = 0
        music = ''
        for j in os.listdir("LevelDefinitions"):
            if i[1] == j:
                p = open(f"LevelDefinitions/{i[1]}/{i[1]}.path", "r", encoding="utf-8")
                pd = json.load(p)
                mpaths = []


                for k in pd["Nodes"]:
                    mpaths.append(0)
                    xl = k["Points"][0][0]
                    yl = k["Points"][0][1]
                    for m in k["Points"]:
                        mpaths[-1] += math.sqrt(((m[0] - xl) ** 2) + (((m[1] - yl) ** 2)))
                        xl = m[0]
                        yl = m[1]
                hugh = f'"{i[1]}":'

                g = 0
                for z in mpaths:
                    print(i[1], f"{z:.2f}")
                    totallength += z

                p.close()


                m = open(f"LevelDefinitions/{i[1]}/{i[1]}.map", "r", encoding="utf-8")
                md = json.load(m)

                music = md["Music"] if "Music" in md else ""

                m.close()

        patht = []

        if i[1] in lengths2:
            for x in lengths2[i[1]]:
                patht.append(str(round(x,2)))
                

        

        o.write(f'''{{{{-start-}}}}
\'\'\'{namess[i[1]]}\'\'\'
{{{{stub}}}}{f"{nl}{{{{screenshot needed|console version}}}}" if c == 1 else ''}
{{{{BTD5 track info
|id F=
|id D={"""
|id C=""" if c == 1 else ""}{i[1] if c == 1 else ""}
|id M={i[1]}

|name F ={namess[i[1]]}
|name M ={namess[i[1]]}
|image F=BTD5F {namess[i[1]]}.png
|image M=BTD5M {i[1]}_thumb.jpg{"""
|image C=""" if c == 1 else ""}

|difficulty F={"Extreme" if i[0] == 4 else "Expert" if i[0] == 3 else "Advanced" if i[0] == 2 else "Intermediate" if i[0] == 1 else "Beginner"}
|difficulty M={"Extreme" if i[0] == 4 else "Expert" if i[0] == 3 else "Advanced" if i[0] == 2 else "Intermediate" if i[0] == 1 else "Beginner"}
|music F     =
|music D     =
|music M     ={"Volcano Theme" if music == "volcano.mp3" else "Main Theme" if music == "jazz.mp3" else "Jazz Theme" if music == "main.mp3" else "Volcano Theme" if music == "volcano.mp3" else "Bloons Disco Party" if music == "dance.mp3" else "Bloons Rock Party" if music == "rock.mp3" else "Bloons House Party" if music == "electro.mp3" else music}
|solo F      =Yes
|coop F      =
|solo M      =Yes{"""
|coop M      =y""" if coop else ""}
|solo C      =Yes{"""
|coop C      =y""" if coop else ""}

|entrances=1
|exits    =1
|junctions=0
|tunnels  =0
|water    ={"Yes" if water else "No"}
|path lengths F=
|path lengths M={totallength:.2f}
}}}}
\'\'\'{namess[i[1]]}\'\'\' is {"an [[Extreme" if i[0] == 4 else "an [[Expert" if i[0] == 3 else "an [[Advanced" if i[0] == 2 else "an [[Intermediate" if i[0] == 1 else "a [[Beginner"}]] [[Map|track]] in ''[[Bloons TD 5]]''.

==Layout==
{{{{empty}}}}
{{{{clear|right}}}}
==Navigation==
{{{{BTD5M track nav}}}}{"""
{{BTD5C track nav}}""" if c == 1 else ''}
{{{{BTD5F track nav}}}}
{{{{BTD5D track nav}}}}
{{{{-stop-}}}}
''')

o.close()
tl.close()
ctl.close()
btl.close()