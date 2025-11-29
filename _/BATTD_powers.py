import xml.etree.ElementTree as ET
import json
import itertools

x = 0
y = 0

def g(lang):
    return lang[0][7][0][x][y].text

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

f = open('MonoBehaviour/PlayerPowers.json', 'r')
d = json.load(f)

o = open('pywiki_BATTD_powers.txt','w',encoding="utf-8")

for i in d["m_allNodes"]:
    if i["m_nodeInstance"]["m_className"] == "Assets.Scripts.Models.Towers.TowerGraph.PlayerPowerNode":
        dx = json.loads(i["m_nodeInstance"]["m_instanceData"])

        if dx["isEnabled"] == False: continue

        x = 0
        y = 0

        for j in range(5):
            for k in range(len(en[0][7][0][j])):
                if en[0][7][0][j][k].attrib["id"] == i["m_name"]:
                    x = j
                    y = k
                    break

        desc = ''

        rarity = ''

        match dx["rarity"]:
            case 0:
                rarity = f'a{"n unused" if dx["isEnabled"] == False else ""} Common'
            case 1:
                rarity = f'an{" unused" if dx["isEnabled"] == False else ""} Uncommon'
            case 2:
                rarity = f'a{"n unused" if dx["isEnabled"] == False else ""} Rare'
            case 3:
                rarity = f'a{"n unused" if dx["isEnabled"] == False else ""} Super Rare'
            case 4:
                rarity = f'an{" unused" if dx["isEnabled"] == False else ""} Epic'

        def desc(lang):
            for j in range(5):
                for k in lang[0][7][1][j]:
                    if k.attrib["id"] == "{0}_desc".format(i["m_name"]):
                        return k.text

        o.write(f'''{{{{-start-}}}}
{{{{bot generated}}}}
{{{{BATTD power info
|id    ={i["m_name"]}

|name       ={g(en)}
|icon       =BATTD power icon {g(en).lower()}.png
|description={desc(en)}

|rarity  ={'Common' if dx["rarity"] == 0 else 'Uncommon' if dx["rarity"] == 1 else 'Rare' if dx["rarity"] == 2 else 'Super Rare' if dx["rarity"] == 3 else 'Epic'}
|quality ={'Small' if dx["quality"] == 0 else 'Medium' if dx['quality'] == 1 else 'Large'}
}}}}
The \'\'\'{g(en)}\'\'\' is {rarity} [[power]] in ''[[Bloons Adventure Time TD]]''.

==In other languages==
{{{{BATTD langs
|da name          ={g(da)}
|da description   ={desc(da)}
|de name          ={g(de)}
|de description   ={desc(de)}
|es name          ={g(es)}
|es description   ={desc(es)}
|fr name          ={g(fr)}
|fr description   ={desc(fr)}
|it name          ={g(it)}
|it description   ={desc(it)}
|ja name          ={g(ja)}
|ja description   ={desc(ja)}
|ko name          ={g(ko)}
|ko description   ={desc(ko)}
|nl name          ={g(nl)}
|nl description   ={desc(nl)}
|no name          ={g(no)}
|no description   ={desc(no)}
|pt-br name       ={g(ptbr)}
|pt-br description={desc(ptbr)}
|ru name          ={g(ru)}
|ru description   ={desc(ru)}
|sv name          ={g(sv)}
|sv description   ={desc(sv)}
|tr name          ={g(tr)}
|tr description   ={desc(tr)}
}}}}

==Navigation==
{{{{BATTD power nav}}}}
{{{{-stop-}}}}
''')


o.close()
f.close()