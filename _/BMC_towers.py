import xml.etree.ElementTree as ET
import os
import json

en = ET.parse('English.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()

fids  =["MonkeySub", "HeliPilot","Bloonchipper", "BananaFarmer"]
fcosts=[200,360,350,350,500,650,300,270,500,925,3500,550,1600,1000,750,950,825,450,"",""]
funls =[1,2,3,4,6,7,8,9,11,12,13,14,15,16,17,18,19,20,"",""]
fkeys =['Q','W','E','R','T','Y','A','S','D','F','G','H','C','V','B','N','M','L']
fdescs=["Shoots a single dart that pops a single bloon. A good, cheap tower suitable for the early rounds.",
"Shoots 8 tacks spread in all directions, each tack can pop 1 bloon. Has short range and medium-slow fire rate.",
"Armed with a high-tech long range rifle, pops 2 layers off of bloons with unlimited range.",
"Throws a single boomerang in an arc back round to the monkey. Each boomerang can pop 3 bloons.",
"Stealthy tower that can see Camo Bloons and throws sharp shurikens rapidly.",
"Shoots a single bomb that explodes in a radius burst on impact. Good range, medium-slow fire rate. Can pop lead bloons but not black bloons.",
"Freezes bloons in its burst radius for a short time. Frozen bloons are immune to sharp objects.",
"Shoots a glob of monkey glue at a single bloon. Glued bloons move more slowly than normal.",
"Monkey Buccaneers can only be placed on water. Shoots a single, heavy dart that can pop up to 5 bloons each.",
"Patrols the skies above the action, regularly strafing the area with powerful darts in 8 directions.",
"Throws darts incredibly fast. Has long range and lots of insanely powerful upgrades.",
"Trained in the arts of monkey magic, the Monkey Apprentice weaves magical bolts of power that pop bloons. Each shot can pop 2 bloons. Can upgrade to cast additional spells.",
"Monkey Village does not attack bloons but instead lowers cost of all towers and upgrades in radius by 10%. Has many useful upgrades that help nearby towers.",
"Banana Farms grow bananas that you can collect to turn into cash. When your farm produces some bananas, collect them by moving your mouse over them. Don't leave them too long however, or they will spoil!",
"Targets a specific bit of ground anywhere on the screen. Launches explosive mortar shells to that spot. Useful for placing far away from the track to make room for other towers.",
"Shoots darts like a machine gun, super fast but not very accurate. The Dartling Gun will shoot towards wherever your mouse is, so you control how effective it is!",
"Generates piles of road spikes on bits of nearby track. Each pile can pop 5 bloons, and unused spikes disappear at the end of each round.",
"Good at building stuff, the Engineer shoots bloons with a powerful nail gun, and has many useful upgrades that create traps, sentries and other enhancements."]

a = open("pywiki_BMC_towers.txt", "w", encoding="utf-8")

t = ""


toword = """{
	"Items" : [
	   { "Icon" : "dart_monkey_icon", "FactoryName" : "DartMonkey", "ObjectType" : 0, "KeyboardShortcut" : "q" },
	   { "Icon" : "sniper_icon", "FactoryName" : "SniperMonkey", "ObjectType" : 0, "KeyboardShortcut" : "e" },
	   { "Icon" : "ninja_icon", "FactoryName" : "NinjaMonkey", "ObjectType" : 0, "KeyboardShortcut" : "t" },
	   { "Icon" : "ice_icon", "FactoryName" : "IceTower", "ObjectType" : 0, "KeyboardShortcut" : "a" },
	   { "Icon" : "buccaneer_icon", "FactoryName" : "MonkeyBuccaneer", "ObjectType" : 0, "KeyboardShortcut" : "d" },
	   { "Icon" : "supermonkey_icon", "FactoryName" : "SuperMonkey", "ObjectType" : 0, "KeyboardShortcut" : "g" },
	   { "Icon" : "village_icon", "FactoryName" : "MonkeyVillage", "ObjectType" : 0, "KeyboardShortcut" : "c" },
	   { "Icon" : "mortar_icon", "FactoryName" : "MortarTower", "ObjectType" : 0, "KeyboardShortcut" : "b" },
	   { "Icon" : "spike_factory_icon", "FactoryName" : "SpikeFactory", "ObjectType" : 0, "KeyboardShortcut" : "m" },
       { "Icon" : "engineer_icon", "FactoryName" : "MonkeyEngineer", "ObjectType" : 0, "KeyboardShortcut" : "l" },
       { "Icon" : "tack_shooter_icon", "FactoryName" : "TackTower", "ObjectType" : 0, "KeyboardShortcut" : "w" },
       { "Icon" : "boomerang_icon", "FactoryName" : "BoomerangThrower", "ObjectType" : 0, "KeyboardShortcut" : "r" },
       { "Icon" : "bomb_icon", "FactoryName" : "BombTower", "ObjectType" : 0, "KeyboardShortcut" : "y" },
       { "Icon" : "glue_gunner_icon", "FactoryName" : "GlueGunner", "ObjectType" : 0, "KeyboardShortcut" : "s" },
       { "Icon" : "monkey_ace_icon", "FactoryName" : "MonkeyAce", "ObjectType" : 0, "KeyboardShortcut" : "f" },
       { "Icon" : "apprentice_icon", "FactoryName" : "MonkeyApprentice", "ObjectType" : 0, "KeyboardShortcut" : "h" },
       { "Icon" : "banana_farm_icon", "FactoryName" : "BananaFarm", "ObjectType" : 0, "KeyboardShortcut" : "v" },
       { "Icon" : "dartling_gun_icon", "FactoryName" : "DartlingGun", "ObjectType" : 0, "KeyboardShortcut" : "n" },
       { "Icon" : "helicopter_icon", "FactoryName" : "HeliPilot", "ObjectType" : 0, "KeyboardShortcut" : "j" },
       { "Icon" : "bloonchipper_icon", "FactoryName" : "Bloonchipper", "ObjectType" : 0, "KeyboardShortcut" : ";"},
       { "Icon" : "monkeysub_icon", "FactoryName" : "MonkeySub", "ObjectType" : 0, "KeyboardShortcut" : "k" },
       { "Icon" : "farmer_icon", "FactoryName" : "BananaFarmer", "ObjectType" : 0, "KeyboardShortcut" : "u" }
	]
}
"""

tord = json.loads(toword)["Items"]

myms = open("6176_ninjakiwi.monkeyTown.data.RemoteDataManager_JsonData.bin", "r", encoding="utf-8")
mym = json.load(myms)["myMonkeys"]

def g(lang):
	for i in lang[0]:
		for j in i:
			if j.attrib["id"] == f"LOC_MY_MONKEYS_{t}_NAME":
				return j.text

def d(lang):
	for i in lang[0]:
		for j in i:
			if j.attrib["id"] == f"LOC_TOWER_DESC_OSX_{t}":
				return j.text

def dd(lang):
	for i in lang[0]:
		for j in i:
			if j.attrib["id"] == f"LOC_MY_MONKEYS_{t}_DESC":
				return j.text

def ss(lang):
	for i in lang[0]:
		for j in i:
			if j.attrib["id"] == f"LOC_MY_MONKEYS_{t}_STRENGTHS":
				return j.text

def ww(lang):
	for i in lang[0]:
		for j in i:
			if j.attrib["id"] == f"LOC_MY_MONKEYS_{t}_WEAKNESS":
				return j.text

for f in os.listdir("TowerDefinitions"):
	if f[:-6] in fids:
		m = open(f"TowerDefinitions/{f}","r", encoding="utf-8")
		md = json.load(m)
		port = md["Icon"]
		cost = md["BaseCost"]
		m.close()

		t = md["TypeName"]

		x = fids.index(md["TypeName"])

		kb = ""
		for i in tord:
			if i["FactoryName"] == t: kb = i["KeyboardShortcut"].upper()

		icn = ""
		for i in tord:
			if i["FactoryName"] == t: icn = i["Icon"]

		a.write(f'''{{{{-start-}}}}
\'\'\'{g(en)} (BMC)\'\'\'
{{{{for|the {g(en)} in general|{g(en)}}}}}
{{{{bot generated}}}}
{{{{BMC tower info
|id={md["TypeName"]}

|name         ={g(en)}
|image M      =BMCM {port}.png
|icon M       =BTD5M {icn}.png
|description M={d(en)}

|cost M={cost}
|hotkey={kb}

|bio description M={dd(en)}
|bio strengths M  ={ss(en)}
|bio weaknesses M ={ww(en)}
|requires=
|upgrades=
}}}}
The \'\'\'{g(en)}\'\'\' is a [[tower]] in the {{{{mobile version of|Bloons Monkey City}}}}.
{{{{TOC}}}}
{{{{clear|right}}}}
==Upgrades==
{{{{BMC upgrade list by tower|{g(en)}}}}}

==Monkey Knowledge==
{{{{#lst:Monkey Knowledge (BMC)|{g(en)}}}}}

==Gallery==
{{{{main gallery|{g(en)}}}}}

===Screenshots===
{{{{screenshot needed}}}}

===Artwork and icons===
<gallery>
BMCM {port}.png|Mobile portrait
BTD5M {icn}.png|Mobile icon
</gallery>

==Navigation==
{{{{BMC {g(en).lower()} nav}}}}
{{{{BMC tower nav}}}}
{{{{{g(en).lower()} nav}}}}
{{{{-stop-}}}}
''')





a.close()