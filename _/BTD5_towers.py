import xml.etree.ElementTree as ET
import os
import json

en = ET.parse('English.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()

fids  =["DartMonkey","TackTower","SniperMonkey","BoomerangThrower","NinjaMonkey","BombTower","IceTower","GlueGunner","MonkeyBuccaneer","MonkeyAce","SuperMonkey","MonkeyApprentice","MonkeyVillage","BananaFarm","MortarTower","DartlingGun","SpikeFactory","MonkeySub"]
fcosts=[200,360,350,380,500,650,300,270,500,900,3500,550,1600,1000,750,950,750,350,"",""]
funls =[1,2,3,4,6,7,8,9,11,12,13,14,15,16,17,18,19,20,"",""]
fkeys =['Q','W','E','R','T','Y','A','S','D','F','G','H','C','V','B','N','M','J']
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
"Banana Farms grow bananas that you can collect to turn into cash. When your farm produces some bananas, collect them by moving your mouse over them. Don\'t leave them too long however, or they will spoil!",
"Targets a specific bit of ground anywhere on the screen. Launches explosive mortar shells to that spot. Useful for placing far away from the track to make room for other towers.",
"Shoots darts like a machine gun, super fast but not very accurate. The Dartling Gun will shoot towards wherever your mouse is, so you control how effective it is!",
"Generates piles of road spikes on bits of nearby track. Each pile can pop 5 bloons, and unused spikes disappear at the end of each round.",
"Water based tower that shoots homing darts. Can upgrade to shoot at Bloons in the radius of any other tower. Can also upgrade to submerge and become a support tower."]

top = open("TowerOrderTop.json", "r")
td = json.load(top)
bot = open("TowerOrderBottom.json", "r")
bd = json.load(bot)

a = open("pywiki_BTD5_towers.txt", "w", encoding="utf-8")


jeh = 0
des = 0
def g(lang):
    v = lang[0][jeh].text

    return v.replace("\\n"," ")
def d(lang):
    v = lang[0][des].text

    return v.replace("\\n"," ")

for i in bd["Items"]:
	for k in range(len(en[0])):
		t = i["FactoryName"]
		if en[0][k].attrib["id"] == f"LOC_{t}_TOWER":
			jeh = k
		if en[0][k].attrib["id"] == f"LOC_TOWER_DESC_{t}":
			des = k

	port = ""
	cost = 0
	rank = 0

	for k in os.listdir("TowerDefinitions"):
		t = i["FactoryName"]
		if k == f"{t}.tower":
			m = open(f"TowerDefinitions/{k}","r", encoding="utf-8")
			md = json.load(m)
			port = md["Icon"]
			cost = md["BaseCost"]
			rank = md["RankToUnlock"]
			m.close()
			break

	a.write(f'''{{{{-start-}}}}
\'\'\'{g(en)} (BTD5)\'\'\'
{{{{for|the {g(en)} in general|{g(en)}}}}}
{{{{bot generated}}}}
{{{{BTD5 tower info
|id={i["FactoryName"]}

|name         ={g(en)}
|image M      =BTD5M {port}.png
|icon M       =BTD5M {i["Icon"]}.png
|description M={d(en)}
|description C={d(en)}

|cost M  ={cost}
|hotkey M={i["KeyboardShortcut"].upper()}
}}}}
The \'\'\'{g(en)}\'\'\' is a [[tower]] in the {{{{mobile version|Bloons TD 5}}}} and {{{{console version|Bloons TD 5}}}}.
{{{{TOC}}}}
{{{{clear|right}}}}
==Upgrades==
{{{{BTD5 upgrade list by tower|{g(en)}}}}}

==Gallery==
{{{{main gallery|{g(en)}}}}}

===Screenshots===
{{{{screenshot needed}}}}

===Assets===
<gallery>
BTD5M {port}.png|Portrait
BTD5M {i["Icon"]}.png|Icon
</gallery>

==In other languages==
{{{{BTD5M text list by key|LOC_{t}_TOWER|label=Name}}}}
{{{{BTD5M text list by key|LOC_TOWER_DESC_{t}|label=Description}}}}

==Navigation==
{{{{BTD5 {g(en).lower()} nav}}}}
{{{{BTD5 tower nav}}}}
{{{{{g(en).lower()} nav}}}}
{{{{-stop-}}}}
''')





a.close()
top.close()
bot.close()