import xml.etree.ElementTree as ET
import json

en = ET.parse('English.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()

o = open("pywiki_BMC_mvm_buildings.txt", "w", encoding="utf-8")

fd = json.load(open('12077_ninjakiwi.monkeyTown.data.RemoteDataManager_JsonData.json'))
md = json.load(open('buildingDataPVP.json'))

def terrain(id):
    match id:
        case 'LakeTerrain': return '[[Lake Terrain]]'
        case 'RiverTerrain': return '[[River Terrain]]'
        case 'MountainTerrain': return '[[Mountain Terrain]]'
        case 'JungleTerrain': return '[[Jungle Terrain]]'
        case 'WaterEdge': return "<abbr title='Adjacent to a River or Lake tile'>Water's Edge Terrain</abbr>"
        case 'VolcanoTerrain': return '[[Volcano Terrain]]'
        case 'StickySapPlant': return '[[Sticky Sap Plant|Sticky Sap Plant Terrain]]'
        case 'ConsecratedGround': return '[[Consecrated Ground|Consecrated Ground Terrain]]'
        case 'SnowTerrain': return '[[Snow Terrain]]'
        case _: return id

def terrainprop(id):
    match id:
        case 'StickySapPlant': return '[[Sticky Sap Plant|Sticky Sap Plant Terrain]]'
        case 'ConsecratedGround': return '[[Consecrated Ground|Consecrated Ground Terrain]]'
        case 'PhaseCrystal': return '[[Phase Crystal|Phase Crystal Terrain]]'
        case _: return "AAAAAAAA " + id

def monkeyAsLink(id):
    if id == "DartMonkey":              return "[[Dart Monkey (BMC)|]]s"
    elif id == "BoomerangThrower":      return "[[Boomerang Thrower (BMC)|]]s"
    elif id == "SniperMonkey":          return "[[Sniper Monkey (BMC)|]]s"
    elif id == "NinjaMonkey":           return "[[Ninja Monkey (BMC)|]]s"
    elif id == "BombTower":             return "[[Bomb Shooter (BMC)|]]s"
    elif id == "IceTower":              return "[[Ice Monkey (BMC)|]]s"
    elif id == "TackTower":             return "[[Tack Shooter (BMC)|]]s"
    elif id == "GlueGunner":            return "[[Glue Gunner (BMC)|]]s"
    elif id == "MonkeyBuccaneer":       return "[[Monkey Buccaneer (BMC)|]]s"
    elif id == "MonkeyAce":             return "[[Monkey Ace (BMC)|]]s"
    elif id == "SuperMonkey":           return "[[Super Monkey (BMC)|]]s"
    elif id == "MonkeyApprentice":      return "[[Monkey Apprentice (BMC)|]]s"
    elif id == "MortarTower":           return "[[Mortar Monkey (BMC)|]]s"
    elif id == "SpikeFactory":          return "[[Spike Factory (BMC)|Spike Factories]]"
    elif id == "DartlingGun":           return "[[Dartling Gun (BMC)|]]s"
    elif id == "ExplodingPineapple":    return "[[Exploding Pineapple (BMC)|]]s"
    elif id == "RoadSpikes":            return "[[Road Spikes (BMC)|]]"
    elif id == "MonkeyVillage":         return "[[Monkey Village (BMC)|]]s"
    elif id == "MonkeyEngineer":        return "[[Monkey Engineer (BMC)|]]s"
    elif id == "Bloonchipper":          return "[[Bloonchipper (BMC)|]]s"
    elif id == "HeliPilot":             return "[[Heli Pilot (BMC)|]]s"
    elif id == "MonkeySub":             return "[[Monkey Sub (BMC)|]]s"
    elif id == "BananaFarmer":          return "[[Banana Farmer (BMC)|]]s"


vi = 0
for kk, vv in fd['pvpBuildingsData'].items():
    i = vv
    if i["buildingDisplayCategory"] == "PVP":
        vi += 1
        name = ''
        desc = ''
        for j in en[0][14]:
            if j.attrib['id'] == f'LOC_BUILDING_{i["_ID"]}':
                name = j.text
            if j.attrib['id'] == f'LOC_BUILDING_DESC_{i["_ID"]}':
                desc = j.text

        namex = ""

        #if len(i["requiresBuilding"]) > 0: print(i["_ID"])

        inf = '0'
        flashp1 = ''
        flashp2 = ''

        mp1 = f'''
|name M       ={name}
|image M      =
|description M={desc}'''
        
        mp2 = f'''
|cc M   ={i["monkeyMoneyCost"]}
|level M={i["minimumMonkeyTownLevel"]}
|xp M   ={i["xpGivenForBuilding"]}
|power M={i["powerUsed"]}
|time M ={i["timeToBuild"]}'''
        
        if i["_ID"] in fd['pvpBuildingsData']:
            inf = '1'
            flashp1 = f'''
|name F       ={fd['pvpBuildingsData'][i["_ID"]]["name"]}
|name M       ={name}
|image F      =
|image M      =
|description F={fd['pvpBuildingsData'][i["_ID"]]["gameDescription"]}
|description M={desc}'''
            
            if fd['pvpBuildingsData'][i["_ID"]]["name"] != name: namex = f" ('''{fd['pvpBuildingsData'][i['_ID']]['name']}''' in the {{{{Flash version|Bloons Monkey City}}}})"

            flashp2 = f'''
|level F={fd['pvpBuildingsData'][i["_ID"]]["minimumMonkeyTownLevel"]}
|level M={i["minimumMonkeyTownLevel"]}
|cc F   ={fd['pvpBuildingsData'][i["_ID"]]["monkeyMoneyCost"]}
|cc M   ={i["monkeyMoneyCost"]}
|power F={fd['pvpBuildingsData'][i["_ID"]]["powerUsed"]}
|power M={i["powerUsed"]}
|time F ={fd['pvpBuildingsData'][i["_ID"]]["timeToBuild"]}
|time M ={i["timeToBuild"]}
|xp F   ={fd['pvpBuildingsData'][i["_ID"]]["xpGivenForBuilding"]}
|xp M   ={i["xpGivenForBuilding"]}'''
            
        disallowed = ""
        for j in i["disallowTerrain"]:
            disallowed += terrain(j.strip('"'))
            disallowed += ", "

        required = ""
        for j in i["requiresTerrain"]:
            required += terrain(j.strip('"'))
            required += ", "
        #for j in i["requiresTerrainProperty"]:
        #    required += terrainprop(j.strip('"'))
        #    required += ", "

        if len(disallowed) > 0: disallowed = disallowed.rstrip(', ')
        if len(required) > 0: required = required.rstrip(', ')

        o.write(f'''{{{{-start-}}}}
\'\'\'{name}\'\'\'
{{{{bot generated}}}}
{{{{BMC building info
|id={i["_ID"]}
|order={vi}
{flashp1 if i["_ID"] in fd['pvpBuildingsData'] else mp1}

|category          =MVM
|tile footprint x  ={i["footprint"][0]}
|tile footprint y  ={i["footprint"][2]}
|sub footprint x   ={i["mob_footprint"][0]}
|sub footprint y   ={i["mob_footprint"][2]}
|disallowed terrain={disallowed}
|required terrain  ={required}
{flashp2 if i["_ID"] in fd['pvpBuildingsData'] else mp2}
}}}}
The \'\'\'{name}\'\'\'{namex} is an [[MVM Building]] in {"''[[Bloons Monkey City]]''" if i["_ID"] in fd['pvpBuildingsData'] else "the {{mobile version of|Bloons Monkey City}}"}.

==Gallery=={"""
===Mobile version==="""if i["_ID"] in fd['pvpBuildingsData'] else ""}
{{{{image needed|building sprites}}}}
{"""
===Flash version===
{{image needed|building sprites}}"""if i["_ID"] in fd['pvpBuildingsData'] else ""}
{{{{clear|right}}}}
==Navigation==
{{{{BMC building nav}}}}
{{{{-stop-}}}}
''')
        
o.close()