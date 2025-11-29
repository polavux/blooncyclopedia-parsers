import xml.etree.ElementTree as ET
import os
import json

fids  =["MonkeySub", "MonkeyEngineer", "HeliPilot", "Bloonchipper", "CobraMonkey"]
fnames=["Monkey Sub", "Monkey Engineer", "Heli Pilot", "Bloonchipper", "COBRA"]
fcosts=[200,360,350,350,500,650,300,270,500,900,3500,550,1600,1000,750,950,750]
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
"Generates piles of road spikes on bits of nearby track. Each pile can pop 10 bloons, and unused spikes disappear at the end of each round."]


a = open("pywiki_BTDB_towers.txt", "w", encoding="utf-8")


jeh = 0
des = 0

for i in os.listdir("TowerDefinitions"):

	if i[:-6] in fids:
		m = open(f"TowerDefinitions/{i}","r", encoding="utf-8")
		md = json.load(m)
		port = md["Icon"]
		cost = md["BaseCost"]
		rank = md["RankToUnlock"]
		m.close()

		x = fids.index(md["TypeName"])

		a.write(f'''{{{{-start-}}}}
\'\'\'{fnames[x]} (Battles)\'\'\'
{{{{for|the {fnames[x]} in general|{fnames[x]}}}}}
{{{{bot generated}}}}
{{{{BTDB tower info
|id={md["TypeName"]}

|name         ={fnames[x]}
|image M      =BTDBM {port}.png
|icon M       =BTDBM {md["Icon"]}.png
|description M={md["Description"]}

|cost M={cost}
}}}}
The \'\'\'{fnames[x]}\'\'\' is a [[tower]] in the {{{{mobile version of|Bloons TD Battles}}}}.
{{{{TOC}}}}
{{{{clear|right}}}}
==Upgrades==
{{{{BTDB upgrade list by tower|{fnames[x]}}}}}

==Update history==
{{{{BTDB change list by tower|{fnames[x]}}}}}

==Gallery==
{{{{main gallery|{fnames[x]}}}}}

===Screenshots===
{{{{screenshot needed}}}}

===Artwork and icons===
<gallery>
BTDBM {port}.png|Portrait
BTDBM {md["Icon"]}.png|Icon
</gallery>

==Navigation==
{{{{BTDB {fnames[x].lower()} nav}}}}
{{{{BTDB tower nav}}}}
{{{{{fnames[x].lower()} nav}}}}
{{{{-stop-}}}}
''')





a.close()