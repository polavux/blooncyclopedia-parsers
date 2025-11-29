import xml.etree.ElementTree as ET
import os
import json

nn = "\n"

ssssss = []

ptbr = ET.parse('Brazilian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
da = ET.parse('Danish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
nl = ET.parse('Dutch.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
en = ET.parse('English.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
fr = ET.parse('French.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
de = ET.parse('German.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
it = ET.parse('Italian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ja = ET.parse('Japanese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ko = ET.parse('Korean.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
no = ET.parse('Norwegian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ru = ET.parse('Russian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
es = ET.parse('Spanish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
sv = ET.parse('Swedish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
tr = ET.parse('Turkish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()

a = open("data/Achievements.json", "r", encoding="utf-8")
ad = json.load(a)

ass = ET.parse('assets.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()

def get_file(pathid):
    name = ""
    for i in ass:
        for j in i:
            if j.tag == "Name": name = j.text
            if j.tag == "PathID" and j.text == str(pathid): return name

o = open("pywiki_BATTD_achievements.txt", "w", encoding="utf-8")

zzzs = ["ZoneTitle_Grasslands", "ZoneTitle_Candy", "ZoneTitle_Ice", "ZoneTitle_Badlands", "ZoneTitle_FireKingdom", "ZoneTitle_Lemongrab", "ZoneTitle_UnderwaterCity", "ZoneTitle_Swamp", "ZoneTitle_LumpySpace"]

for category in ad['achievementCategories']:
    tlist = 0
    rewardstext = []
    hidden = None

    def dd(l):
        for i in l[0]:
            if "id" in i.attrib and i.attrib['id'] == category['achievementCategory'] + "_0_desc": return i.text
            if len(i) > 0:
                for j in i:
                    if "id" in j.attrib and j.attrib['id'] == category['achievementCategory'] + "_0_desc": return j.text
                    if len(j) > 0:
                        for k in j:
                            if "id" in k.attrib and k.attrib['id'] == category['achievementCategory'] + "_0_desc": return k.text
                            if len(k) > 0:
                                for l in k:
                                    if "id" in l.attrib and l.attrib['id'] == category['achievementCategory'] + "_0_desc": return l.text
        return 'x'

    for achievement in ad['achievements']:
        if achievement['achievementCategory'] == category['achievementCategory']:
            if hidden == None: hidden = achievement['isHidden'] 
            fobj = open("data/" + str(achievement["objective"]["m_PathID"]) + ".json", 'r', encoding='utf-8')
            obj = json.load(fobj)

            tlist +=1

            

            rewards = []

            # REWARDS
            for preward in obj["rewards"]:
                freward = open("data/" + str(preward["m_PathID"]) + ".json", 'r', encoding='utf-8')
                reward = json.load(freward)

                #print(reward["m_Name"], reward["reward"])

                rew = "{{BATTD " + {
                    'WishOrbs': 'wish orb',
                    'Coins': 'coin',
                    'Gems': 'gem',
                    'CosmicEssence': 'resourcedbfsdr',
                    'Shards': 'shard',
                    'Powers': 'power',
                    'TowerXP': 'resource'
                    }[reward["m_Name"]]
                
                if 'rarity' in reward['reward']: rew += "|" + ['Common', 'Uncommon', 'Rare', 'Super Rare', 'Epic'][reward['reward']['rarity']]
                if 'towerType' in reward['reward']: rew += "|" + ['?????????????????', 'Bananas', 'Finn Cakes', 'Meatballs', 'Fan Fiction', 'Firewood', 'Red', 'Candy', 'Dynamite', 'Potions', 'Sushi', 'Idols', 'Anchors'][reward['reward']['towerType']]
                rew +=  "|" + str(reward["reward"]['qty']) + "}}"
                rewards.append(rew)

                '''public const TowerBaseType Max = 1;
	public const TowerBaseType Finn = 2;
	public const TowerBaseType Jake = 3;
	public const TowerBaseType IceKing = 4;
	public const TowerBaseType FlamePrincess = 5;
	public const TowerBaseType Marceline = 6;
	public const TowerBaseType Bubblegum = 7;
	public const TowerBaseType C4Charlie = 8;
	public const TowerBaseType Sam = 9;
	public const TowerBaseType Sai = 10;
	public const TowerBaseType SuperMonkey = 11;
	public const TowerBaseType CaptainCassie = 12;'''

                freward.close()

            rewardstext.append("|description " + str(tlist) + "=" + (dd(en) if dd(en) != 'x' else '') + "\n" + "|rewards " + str(tlist) + "    =" + ', '.join(rewards))

            fobj.close()

    def n(l):
        for i in l[0]:
            if "id" in i.attrib and i.attrib['id'] == category['achievementCategory']: return i.text
            if len(i) > 0:
                for j in i:
                    if "id" in j.attrib and j.attrib['id'] == category['achievementCategory']: return j.text
                    if len(j) > 0:
                        for k in j:
                            if "id" in k.attrib and k.attrib['id'] == category['achievementCategory']: return k.text
                            if len(k) > 0:
                                for l in k:
                                    if "id" in l.attrib and l.attrib['id'] == category['achievementCategory']: return l.text
    #print(hidden)

    if hidden != 0: ssssss.append(n(en))
    o.write(f"""{{{{-start-}}}}
'''{n(en)}'''
{{{{BATTD achievement info
|id={category['achievementCategory']}

|name ={n(en)}
|image=

{nn.join(rewardstext)}

|hidden    ={hidden}
|introduced=
}}}}
'''{n(en)}''' is a{'n' if hidden == 0 else ' hidden'} [[achievement]] in ''[[Bloons Adventure Time TD]]''.

==In other languages==
{{{{BATTD langs
|da name   ={n(da)}
|de name   ={n(de)}
|es name   ={n(es)}
|fr name   ={n(fr)}
|it name   ={n(it)}
|ja name   ={n(ja)}
|ko name   ={n(ko)}
|nl name   ={n(nl)}
|no name   ={n(no)}
|pt-br name={n(ptbr)}
|ru name   ={n(ru)}
|sv name   ={n(sv)}
|tr name   ={n(tr)}
}}}}
{{{{clear|right}}}}
==Navigation==
{{{{BATTD achievement nav}}}}
{{{{-stop-}}}}
""")

ss2 = sorted(ssssss)
ss3 = ""
for i in ss2:
    ss3 += ("[[" + i + "]]{{*}}")

print(ss3)

a.close()
o.close()