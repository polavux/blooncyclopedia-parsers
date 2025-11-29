import xml.etree.ElementTree as ET
import json
import os
import math

def getpaths(f):
    paths = []
    x = ET.parse(f, parser=ET.XMLParser(encoding="utf-8")).getroot()
    #print(f, x[0].attrib["trackName"])

    nodename = "Node_1"
    curlength = 0
    prevnode = x[0][0].text.split(",")

    for i in x[0]:
        if i.tag != nodename:
            paths.append(format(curlength, ".2f"))
            curlength = 0
            nodename = i.tag
            prevnode = i.text.split(",")

        newnode = i.text.split(",")

        curlength += math.sqrt(
            ((float(newnode[0]) - float(prevnode[0]))**2) +
            ((float(newnode[1]) - float(prevnode[1]))**2)
        )
        prevnode = newnode

        
    paths.append(format(curlength, ".2f"))
    #print(f, ','.join(paths))
    return ','.join(paths)

o = open("pywiki_BTD4M_maps.txt", "w", encoding='utf-8')

comp = {
    "Ant_Hill_Paths.xml" : "Ant Hill",
    "Bee_Hive_Paths.xml": "Bee Hive",
    "Bloonraker_Paths.xml":"Bloonraker",
    "Blue_Laser_Paths.xml" : "Blue Laser",
    "Bus_Route_Paths.xml" : 'Bus Route',
    "Cactus_Creek_Paths.xml" : "Cactus Creek",
    "Daisy_Chain_Paths.xml" : "Daisy Chain",
    "Dna_Test_Paths.xml" : "DNA Test",
    "Farm_Yard_Paths.xml" : "Farm Yard",
    "Firecracker_Paths.xml": "Firecracker",
    "Gigapops_Paths.xml": "1.21 Gigapops!",
    "Go_Bananas_Paths.xml" : "Go Bananas!",
    "Halloween_Paths.xml": "Trick or Treat",
    "Jolly_Roger_Paths.xml": "Jolly Roger",
    'Lava_Lake_Paths.xml' : "Lava Lake",
    "Military_Base_Paths.xml" : "Military Base",
    "Milk_And_Cookies_Paths.xml": "Milk 'n' Cookies",
    "Moaby_Dick_Paths.xml": "MOAB-y Dick",
    "Monkeys_Vs_Bloons_Paths.xml": "Monkeys vs Bloons",
    "Monkey_Heart_Paths.xml": "Monkey Heart",
    "Monkey_Temple_Paths.xml" : "Monkey Temple",
    "Ocean_Road_Paths.xml"  : "Ocean Road",
    "Pool_Party_Paths.xml": "Pool Party",
    "Pool_Table_Paths.xml" : "Pool Table",
    "Rail_Track_Paths.xml" : 'Rail Track',
    "River_Bed_Paths.xml" : "River Bed",
    "Snow_Monkey_Paths.xml": "Snow Monkey",
    "Snow_Trail_Paths.xml" : "Snow Trail",
    "Storm_Clouds_Paths.xml" : 'Storm Cloud',
    "Sweet_Tooth_Paths.xml" : "Sweet Tooth",
    "Tannenbaum_Paths.xml": "Tannenbaum",
    "World_Tour_Paths.xml" : "World Tour"
}

for i in os.listdir("ios"):
    print(i)
    if comp[i] not in ["River Bed"]: continue
    #if comp[i] in ['Ant Hill', 'Bee Hive', 'Go Bananas!', 'Trick or Treat', 'Military Base', "Milk 'n' Cookies", "MOAB-y Dick", "Monkey Heart", "Pool Party", "Snow Monkey", 'Bloonraker', 'Blue Laser', 'Bus Route', 'Daisy Chain', 'DNA Test', 'Firecracker', 'Ocean Road', 'Pool Table', 'Rail Track', 'River Bed', 'Sweet Tooth', 'World Tour']: continue
    pathsios = getpaths("ios/" + i)
    pathshd = ""
    if i in os.listdir("ipad"): pathshd = getpaths("ipad/" + i)
    a = i.lower().replace("_paths", "")
    pathsand = ""
    pathsdsi = ""
    if a in os.listdir("and"): pathsand = getpaths("and/" + a)
    if a in os.listdir("dsi"):
        pathsdsi = getpaths("dsi/" + a)
        #if pathsdsi == pathsand: print(i)
    o.write(f"""{{{{-start-}}}}
'''{comp[i]}'''
{{{{stub}}}}
{{{{screenshot needed|DSi version}}}}
{{{{BTD4 track info
|id F  =
|id E  =
|id iOS={i[:-10]}
|id A  ={a[:-4]}
|id C  ={a[:-4] if a in os.listdir("dsi") else ""}

|name F   =
|name M   ={comp[i]}
|image iOS={'BTD4iOS ' + i[:-10] + '.png' if a != '' else ''}
|image HD ={'BTD4HD ' + i[:-10] + '.png' if a != '' else ''}
|image A  ={'BTD4A ' + a[:-3] + 'png' if a != '' else ''}
|image C  =

|difficulty=
|entrances =
|exits     =
|junctions =
|water     =

|path labels     =
|path lengths F  =
|path lengths iOS={pathsios}
|path lengths HD ={pathshd}
|path lengths A  ={pathsand}
}}}}
'''{comp[i]}''' is an ??????? [[Map|track]] in ''[[Bloons TD 4]]''.

==Layout==
{{{{empty}}}}
{{{{clear|right}}}}
==Navigation==
{{{{BTD4M track nav}}}}
{{{{BTD4C track nav}}}}
{{{{BTD4F track nav}}}}
{{{{-stop-}}}}
""")
    
o.close()