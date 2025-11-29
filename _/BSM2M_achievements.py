import xml.etree.ElementTree as ET
import json


en = ET.parse('English.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
da = ET.parse('Danish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
de = ET.parse('German.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
es = ET.parse('Spanish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
fr = ET.parse('French.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
id = ET.parse('Indonesian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
it = ET.parse('Italian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ja = ET.parse('Japanese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ko = ET.parse('Korean.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
nl = ET.parse('Dutch.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
no = ET.parse('Norwegian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ptbr = ET.parse('BrazilianPortuguese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ru = ET.parse('Russian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
sv = ET.parse('Swedish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
tr = ET.parse('Turkish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
zhcn = ET.parse('Simplified Chinese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
zhtw = ET.parse('Traditional Chinese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()

o = open("achievements.json", 'r', encoding='utf-8')
d = json.load(o)

newachs = []

groups = {
    'beginning': 1,
	'levels': 2,
    'blops': 3,
	'bronzemedal': 4,
	'silvermedal': 5,
	'goldmedal': 6,
	'diamondmedal': 7,
	'mixedbadge': 8,
    'dartbadge': 9,
    'rangbadge': 10,
    'bombbadge': 11,
    'magicbadge': 12,
    'energybadge': 13,
    'icebadge': 14,
    'stormbadge': 15,
	'weaponpurchase': 8,
	'monkeystars': 9,
	'research': 10,
	'powerups': 11,
	'goldenbloon': 12,
	'mysterybloon': 13,
	'crates': 14,
	'bloonpops': 15,
	'hidden': 16
}

for i in d['achievements']:

    ach = {
        'id': '',
        'name': '',
        'image': '',
        'description': '',
        'group': '',
        'reward': 0,
        'prereq': '',
        'hidden': False
    }
    ach['id'] = i['name']
    ach['image'] = i['icon']
    
    for j in en[0][8]:
        if i['name'] == j.attrib['id'].replace('LOC_ACHIEVEMENTS_NAME_', ''):
            ach['name'] = j.text

        if i['name'] == j.attrib['id'].replace('LOC_ACHIEVEMENTS_DESC_', ''):
            ach['description'] = j.text

    ach['group'] = groups[i['group']]
    ach['reward'] = i['reward']
    ach['prereq'] = i['achievementreq']
    ach['hidden'] = i['hidden']

    newachs.append(ach)

    #if j.attrib['id'] == 'LOC_ACHIEVEMENTS_DESC_supermonkeypop': print(x)


o.close()

o2 = open('output.json', 'w', encoding='utf-8')

json.dump({ 'data': newachs }, o2)
o2.close()