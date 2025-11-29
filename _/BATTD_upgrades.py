import xml.etree.ElementTree as ET
import json, os

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

o = open("pywiki_BATTD_allies.txt", "w", encoding="utf-8")

m = open("MonoBehaviour/Minions_Common.json", "r", encoding="utf-8")
md = json.load(m)


for i in os.listdir("MonoBehaviour"):
    f = open(f'MonoBehaviour/{i}', "r", encoding='utf-8')
    fd = json.load(f)

    if fd["m_Script"]["m_PathID"] == 8211594766679199408:
        for j in fd["m_allNodes"]:
            jd = json.loads(j["m_nodeInstance"]["m_instanceData"])
            #if 'ignoreCamo' in jd: print(f"{jd['ignoreCamo']} {i}")
         
    f.close()


for i in range(len(en[0])):
    for j in range(len(en[0][i])):
        for k in range(len(en[0][i][j])):
            if en[0][i][j][k].tag == "allies_common": print(i,j,k)


def g(lang):
    return lang[0][6][2][12][nameid].text


for i in md["m_allNodes"]:

    kd = None
    ud = None
    nameid = 0
    desc = ''
    bdesc = ''
    pros = ''
    cons = ''
    drange = 0

    ugcosts = ''
    uglist = ''

    n = json.loads(i["m_nodeInstance"]["m_instanceData"])

    for j in range(len(en[0][6][2][12])):
        if i['m_name'] == en[0][6][2][12][j].attrib['id']:
            nameid = j
            break

    for j in en[0][6][3][12]:
        if f"{i['m_name']}_desc" == j.attrib['id']:
            bdesc = j.text
        if f"{i['m_name']}_pro" == j.attrib['id']:
            pros = j.text
        if f"{i['m_name']}_con" == j.attrib['id']:
            cons = j.text

    for j in en[0][6][5][0]:
        if f"{i['m_name']}_short" == j.attrib['id']:
            desc = j.text
            break

    # get ally file
    for j in os.listdir("MonoBehaviour"):
        if i['m_name'] in j and "Powers" not in j:
            f = open(f'MonoBehaviour/{j}', "r", encoding='utf-8')
            fd = json.load(f)

            if fd["m_Script"]["m_PathID"] == 8211594766679199408:
                for k in fd["m_parameters"]["instances"]:
                    if "range:" in k["m_instanceData"]:

                        print(i['m_name'])
                        print(k["m_instanceData"])
                        drange = int((k["m_instanceData"]).strip("range:"))
                        print(drange)

                for k in fd["m_allNodes"]:

                    if k["m_nodeInstance"]["m_className"] == "Assets.Scripts.Models.Towers.TowerGraph.SubTowerNode":
                        kd = json.loads(k["m_nodeInstance"]["m_instanceData"])

                    if k["m_nodeInstance"]["m_className"] == "Assets.Scripts.Models.Towers.TowerGraph.TowerUpgrade":
                        ud = json.loads(k["m_nodeInstance"]["m_instanceData"])

                        ugcosts += f"|{ud['cost']}"
            f.close()

    o.write(f'''{{{{-start-}}}}
\'\'\'{g(en)}\'\'\'
{{{{stub}}}}
{{{{BATTD ally infobox
|id={i['m_name']}

|name       ={g(en)}
|image      =
|description={desc}
           
|rarity=Common
|cost  ={kd['cost']}
|count ={n['minions'][0]['count']}

|bio description={bdesc}
|bio strengths  ={pros}
|bio weaknesses ={cons}
}}}}
The \'\'\'{en[0][6][2][12][nameid].text}\'\'\' is a Common [[ally (BATTD)|]] in ''[[Bloons Adventure Time TD]]''.

==Upgrades==

==Stats==
{{{{BATTD tower properties
|footprint    ={kd['placementRadius']}
|flying       ={1 if 'isFlying' in kd and kd['isFlying'] == True else 0}
|placeable on ={
    "Land"                      if kd['placeableArea'] == 1 else
    "Water"                     if kd['placeableArea'] == 2 else
    "Land, water"               if kd['placeableArea'] == 3 else
    "Lava"                      if kd['placeableArea'] == 4 else
    "Land, lava"                if kd['placeableArea'] == 5 else
    "Water, lava"               if kd['placeableArea'] == 6 else
    "Land, water, lava"         if kd['placeableArea'] == 7 else
    "Track"                     if kd['placeableArea'] == 8 else
    "Land, track"               if kd['placeableArea'] == 9 else
    "Water, track"              if kd['placeableArea'] == 10 else
    "Land, water, track"        if kd['placeableArea'] == 11 else
    "Lava, track"               if kd['placeableArea'] == 12 else
    "Land, lava, track"         if kd['placeableArea'] == 13 else
    "Water, lava, track"        if kd['placeableArea'] == 14 else
    "Land, water, lava, track"  if kd['placeableArea'] == 15 else
    "???"}
|display range={drange}
}}}}
===Prices===
{{{{BATTD ally price list|{kd['cost']}{ugcosts}}}}}

==Strategy==
{{{{strategy needed}}}}

==Gallery==
===Screenshots===
{{{{screenshot needed}}}}
===Icons===
<gallery>

</gallery>

==In other languages==
{{{{BATTD langs
|da   ={g(da)}
|de   ={g(de)}
|es   ={g(es)}
|fr   ={g(fr)}
|it   ={g(it)}
|ja   ={g(ja)}
|ko   ={g(ko)}
|nl   ={g(nl)}
|no   ={g(no)}
|pt-br={g(ptbr)}
|ru   ={g(ru)}
|sv   ={g(sv)}
|tr   ={g(tr)}
}}}}

==Navigation==
{{{{BATTD ally navbox}}}}
{{{{-stop-}}}}
''')




m.close()
o.close()