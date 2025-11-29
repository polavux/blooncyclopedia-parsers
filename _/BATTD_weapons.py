import xml.etree.ElementTree as ET
import json, os

itemtype = 10

def g(lang, id):
    return lang[0][6][2][itemtype][id].text

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

weapons = dict()
weaponmods = dict()
op5 = []

p = open('pywiki_BATTD_weapons.txt', 'w', encoding="utf-8")

def loopy(nam):
    g = open(f'MonoBehaviour/{nam}.json', 'r', encoding='utf-8')
    d = json.load(g)

    dat = dict()

    # root
    if d["m_Script"]["m_PathID"] == 8789258266633866180:
        for i in d["modBehaviours"]["behaviours"]:
            dat.update(loopy(i['Id']))
    # cooldown
    elif d["m_Script"]["m_PathID"] == 6678091555332585960:
            dat['speed'] = d["multiplier"]["expression"].replace(' ', '')
    # range
    elif d["m_Script"]["m_PathID"] == -2121708663799993517:
            dat['range'] = d["additive"]["expression"].replace(' ', '')
    # pierce
    elif d["m_Script"]["m_PathID"] == -1995780576697820314:
            dat['pierce'] = d["additive"]["expression"].replace(' ', '')
    # damage
    elif d["m_Script"]["m_PathID"] == 2196490171450557434:
            dat['damage'] = d["additive"]["expression"].replace(' ', '')


    g.close()
    #print(dat)

    return dat

modifiers = dict()
modifiers2 = dict()

restrictionss = dict()

restrictions = {
    'Instrument': 'Jake,Marceline,SerenadingJake',
    'Sword': 'Finn,WarmasterBubblegum,WarriorFinn',
    'Bomb': 'C4Charlie,CaptainCassie',
    'Darts': 'CommanderCassie,JuggernautMax,MarcelineTheVampireHunter,Max,Sai,Supermonkey',
    'Gun': 'Bubblegum',
    'Wand': 'FlamePrincess,IceKing,Sam'
}

for i in os.listdir('MonoBehaviour'):
    f = open(f'MonoBehaviour/{i}', 'r', encoding='utf-8')
    fd = json.load(f)

    if fd["m_Script"]["m_PathID"] == 8211594766679199408:
        for j in fd["m_allNodes"]:
            if j['m_nodeInstance']['m_className'] == "Assets.Scripts.Models.Towers.TowerGraph.TowerEquipmentNode":
                dat = json.loads(j['m_nodeInstance']["m_instanceData"])
                if dat['slotType'] == 0:
                    #print(dat['itemType'], j["m_name"])
                    weapons[j['m_name']] = dat

                    #print(j['m_name'], dat['restrictedTowers'])
                    #print(dat['invertRestrictions'])
                    rest = []
                    if len(dat['restrictedTowers']) != 0:
                        for zzz in dat['restrictedTowers']:
                            rest.append(zzz['Id'])
                        
                        restrictionss[j['m_name']] = (','.join(rest))
                    else:
                        restrictionss[j['m_name']] = restrictions[dat['itemType']]
                    
                    for k in dat['modifiers']:
                        modifiers[j['m_name']] = k['Id']
                        modifiers2[k['Id']] = j['m_name']
                    if i == 'Equipment_1_5.json': op5.append(j['m_name'])

        for j in fd["m_allNodes"]:
            cname = (j['m_name'])
            if cname in modifiers2 and j['m_nodeInstance']['m_className'] == "Assets.Scripts.Models.Towers.TowerGraph.ModelModifierNode":
                dat = json.loads(j['m_nodeInstance']["m_instanceData"])

                parms = dict()
                for k in dat['applyModBehaviours']["behaviours"]:
                    parms.update(loopy(k['Id']))

                #weaponmods[cname] = parms
                newparms = {
                    'range base': '',
                    'range add': '',
                    'range per stars': '',
                    'pierce base': '',
                    'pierce add': '',
                    'pierce per stars': '',
                    'damage base': '',
                    'damage add': '',
                    'damage per stars': '',
                    'speed base': '',
                    'speed add': '',
                    'speed per stars': ''
                }
                if 'range' in parms:
                    newparms['range base'] = parms['range'].split('+')[0]

                    if '+level' in parms['range']: newparms['range add'] = '1'
                    else: newparms['range add'] = (parms['range'].split('+(')[1]).split('*(level')[0]

                    newparms['range per stars'] = 1
                    
                    #print(parms['range'], '        ', cname) 
                    #print(newparms['range base'], '', newparms['range add'])

                if 'pierce' in parms:
                    newparms['pierce base'] = parms['pierce'].split('+')[0]
                    if '/' in parms['pierce']: newparms['pierce per stars'] = parms['pierce'].split('/')[1][0]
                    else: newparms['pierce per stars'] = '1'

                    if cname == '4DSword_modifier': newparms['pierce add'] = '3'
                    elif cname == 'WizardLordWand_modifier': newparms['pierce add'] = '2'
                    elif cname == 'Moap_mod': newparms['pierce add'] = '3'
                    else: newparms['pierce add'] = '1'

                    #print(parms['pierce'], '        ', cname) 
                    
                if 'damage' in parms:

                    #print(parms['damage'], '        ', cname) 
                    newparms['damage base'] = parms['damage'][0]

                    if cname != 'JakesViola_modifier':
                        newparms['damage add'] = '1'
                        newparms['damage per stars'] = parms['damage'][-2]
                        #print(parms['damage'][-2])

                if 'speed' in parms:
                    #print(parms['speed'], '        ', cname) 

                    newparms['speed base'] = parms['speed'].split('+')[0]
                    
                    if cname != 'CandyCaneShotgun_modifier':
                        newparms['speed per stars'] = '2' if '/' in parms['speed'] else '1'
                        newparms['speed add'] = parms['speed'].split("+(")[1].split("*")[0] if "+(" in parms['speed'] else parms['speed'].split("+")[1].split("*")[0]

                        #newparms['speed base'] = newparms['speed base'].replace('1.', '')
                        #newparms['speed add'] = newparms['speed add'].replace('0.0', '')
                    
                weaponmods[modifiers2[cname]] = newparms

    f.close()

rarity = {
    0: 'Common',
    1: 'Uncommon',
    2: 'Rare',
    3: 'Super Rare',
    4: 'Epic',
    5: 'Legendary',
    6: 'Martian'
}

for k,v in weapons.items():

    def n(lan):
        for a in lan[0]:
            for b in a:
                for c in b:
                    for d in c:
                        if 'id' in d.attrib and d.attrib['id'] == k:
                            return d.text
                    
    def d(lan):
        for a in lan[0]:
            for b in a:
                for c in b:
                    for d in c:
                        if 'id' in d.attrib and d.attrib['id'] == f'{k}_desc':
                            return d.text
                    
    def sp(lan):
        for a in lan[0]:
            for b in a:
                for c in b:
                    for d in c:
                        if 'id' in d.attrib and d.attrib['id'] == f'{k}_special':
                            return d.text
        return ''

    rest = restrictions[v['itemType']]

    p.write(f"""{{{{-start-}}}}
'''{n(en)}'''
{{{{bot generated}}}}
{{{{BATTD weapon info
|id={k}

|name       ={n(en)}
|image      =BATTD {n(en)} icon.png
|description={d(en)}

|rarity       ={rarity[v['rarity']]}
|type         ={v['itemType']}
|equippable to={restrictionss[k]}
|introduced   ={'1.5' if k in op5 else ''}

|speed base      ={weaponmods[k]['speed base']}
|speed add       ={weaponmods[k]['speed add']}
|speed per stars ={weaponmods[k]['speed per stars']}
|range base      ={weaponmods[k]['range base']}
|range add       ={weaponmods[k]['range add']}
|range per stars ={weaponmods[k]['range per stars']}
|damage base     ={weaponmods[k]['damage base']}
|damage add      ={weaponmods[k]['damage add']}
|damage per stars={weaponmods[k]['damage per stars']}
|pierce base     ={weaponmods[k]['pierce base']}
|pierce add      ={weaponmods[k]['pierce add']}
|pierce per stars={weaponmods[k]['pierce per stars']}
|special         ={sp(en)}
}}}}
The '''{n(en)}''' is a{'n' if (rarity[v['rarity']] == 'Epic' or rarity[v['rarity']] == 'Uncommon') else ''} {rarity[v['rarity']]} [[Weapon (BATTD)|{v['itemType'].lower()} weapon]] in ''[[Bloons Adventure Time TD]]''.

==Gallery==
{{{{screenshot needed}}}}

==In other languages==
{{{{BATTD langs
|da name          ={n(da)}
|da description   ={d(da)}
|de name          ={n(de)}
|de description   ={d(de)}
|es name          ={n(es)}
|es description   ={d(es)}
|fr name          ={n(fr)}
|fr description   ={d(fr)}
|it name          ={n(it)}
|it description   ={d(it)}
|ja name          ={n(ja)}
|ja description   ={d(ja)}
|ko name          ={n(ko)}
|ko description   ={d(ko)}
|nl name          ={n(nl)}
|nl description   ={d(nl)}
|no name          ={n(no)}
|no description   ={d(no)}
|pt-br name       ={n(ptbr)}
|pt-br description={d(ptbr)}
|ru name          ={n(ru)}
|ru description   ={d(ru)}
|sv name          ={n(sv)}
|sv description   ={d(sv)}
|tr name          ={n(tr)}
|tr description   ={d(tr)}
}}}}
{{{{clear|right}}}}
==Navigation==
{{{{BATTD weapon nav}}}}
{{{{-stop-}}}}
""")

f.close()


exit()

for z in data['m_allNodes']:
    if z['m_nodeInstance']['m_className'] == 'Assets.Scripts.Models.Towers.TowerGraph.TowerEquipmentNode':
        id = z['m_name']

        speedbase = ''
        speedadd = ''
        speedstars = ''
        rangebase = ''
        rangeadd = ''
        rangestars = ''
        damagebase = ''
        damageadd = ''
        damagestars = ''
        piercebase = ''
        pierceadd = ''
        piercestars = ''
        datax = json.loads(z['m_nodeInstance']['m_instanceData'])
        typet = datax['itemType']
        rarity = datax['rarity']

        c4c = 1
        cap = 1

        if len(datax['restrictedTowers']) > 0:
            c4c = 0
            cap = 0
        for u in datax['restrictedTowers']:
            if u['Id'] == 'C4Charlie': c4c = 1
            if u['Id'] == 'CaptainCassie': cap = 1
    
        for i in data['m_allNodes']:
            if i['m_nodeInstance']['m_className'] == 'Assets.Scripts.Models.Towers.TowerGraph.ModelModifierNode' and i['m_name'] in z['m_nodeInstance']['m_instanceData']:
                amb = json.loads(i['m_nodeInstance']['m_instanceData'])
                
                beh = amb['applyModBehaviours']['behaviours'][0]['Id']
                print(id)
                #print(beh)

                f2 = open('json/{0}.json'.format(beh), 'r')

                data2 = json.load(f2)

                #print(data2['modBehaviours']['behaviours'])

                for j in data2['modBehaviours']['behaviours']:
                    f3 = open('json/{0}.json'.format(j['Id']), 'r')
                    data3 = json.load(f3)
                    if data3['m_Script']['m_PathID'] == 6678091555332585960:
                        for s in data3['multiplier']['expression']:
                            if s == '+' or s ==' ': break
                            speedbase += s

                        speedbase = float(speedbase)

                        start_count = False
                        for s in data3['multiplier']['expression']:
                            if s == '(': start_count = True
                            if s == '*' or s=='l': break
                            if start_count and (s.isnumeric() or s == '.'): speedadd += s
                        speedadd = float(speedadd)

                        start_count = False
                        if(len(data3['multiplier']['expression'])) > 1: speedstars = '1'
                        for s in data3['multiplier']['expression']:
                            if s == '/':
                                start_count = True
                                speedstars = ''
                            if start_count and s.isnumeric(): speedstars += s
                        speedstars = int(speedstars)
                    elif data3['m_Script']['m_PathID'] == 2196490171450557434:
                        for s in data3['additive']['expression']:
                            if s == '+' or s ==' ': break
                            damagebase += s
                        damagebase = int(damagebase)

                        start_count = False
                        for s in data3['additive']['expression']:
                            if s == '(': start_count = True
                            if s == '*' or s=='l': break
                            if start_count and s.isnumeric(): damageadd += s
                        if damageadd != '': damageadd = int(damageadd)

                        start_count = False
                        if(len(data3['additive']['expression'])) > 1: damagestars = '1'
                        for s in data3['additive']['expression']:
                            if s == '/':
                                start_count = True
                                damagestars = ''
                            if start_count and s.isnumeric(): damagestars += s
                        damagestars = int(damagestars)
                    elif data3['m_Script']['m_PathID'] == -2121708663799993517:
                        for s in data3['additive']['expression']:
                            if s == '+' or s ==' ': break
                            rangebase += s
                        rangebase = int(rangebase)

                        start_count = False
                        for s in data3['additive']['expression']:
                            if s == '(': start_count = True
                            if s == '*' or s=='l': break
                            if start_count and (s.isnumeric() or s == '.'): rangeadd += s
                        if rangeadd != '': rangeadd = float(rangeadd)

                        start_count = False
                        if(len(data3['additive']['expression'])) > 1: rangestars = '1'
                        for s in data3['additive']['expression']:
                            if s == '/':
                                start_count = True
                                rangestars = ''
                            if start_count and s.isnumeric(): rangestars += s
                        rangestars = int(rangestars)
                    elif data3['m_Script']['m_PathID'] == -1995780576697820314:
                        for s in data3['additive']['expression']:
                            if s == '+' or s ==' ': break
                            piercebase += s
                        piercebase = int(piercebase)

                        start_count = False
                        for s in data3['additive']['expression']:
                            if s == '(': start_count = True
                            if s == '*' or s=='l': break
                            if start_count and s.isnumeric(): pierceadd += s
                        if pierceadd != '': pierceadd = int(pierceadd)

                        start_count = False
                        if(len(data3['additive']['expression'])) > 1: piercestars = '1'
                        for s in data3['additive']['expression']:
                            if s == '/':
                                start_count = True
                                piercestars = ''
                            if start_count and s.isnumeric(): piercestars += s
                        piercestars = int(piercestars)

                    f3.close()

                f2.close()

    #p.write(st.format())

        #y = len(en[0][6][2][itemtype])
        #print(y)
        l = 0
    
        for c in range(len(en[0][6][2][itemtype])):
            if en[0][6][2][itemtype][c].attrib['id'] == id:
                l = c
                break

        o = ''
    
        for c in range(len(en[0][6][4][itemtype])):
            if id in en[0][6][4][itemtype][c].attrib['id']:
                print(en[0][6][4][itemtype][c].text)
                o = en[0][6][4][itemtype][c].text
                break

        p.write(f'''{{{{-start-}}}}
\'\'\'{g(en,l)}\'\'\'
{{{{stub}}}}
{{{{BATTD weapon infobox
|id={id}

|name       ={g(en,l)}
|image      =BATTD {g(en,l)} icon.png
|description={en[0][6][3][itemtype][l].text}

|rarity={rarity}
|type  ={typet}

|C4Charlie    ={c4c}
|CaptainCassie={cap}

|speed base      ={speedbase}
|speed add       ={speedadd}
|speed per stars ={speedstars}
|range base      ={rangebase}
|range add       ={rangeadd}
|range per stars ={rangestars}
|damage base     ={damagebase}
|damage add      ={damageadd}
|damage per stars={damagestars}
|pierce base     ={piercebase}
|pierce add      ={pierceadd}
|pierce per stars={piercestars}
|special         ={o}
}}}}
The \'\'\'{g(en,l)}\'\'\' is {'a [[Rarity (BATTD)|rare]]' if rarity == 2 else 'a [[Rarity (BATTD)|super rare]]' if rarity == 3 else 'an [[Rarity (BATTD)|epic]]' if rarity == 4 else 'a [[Rarity (BATTD)|legendary]]' if rarity == 5 else 'a [[Martian Trader]]-exclusive' if rarity == 6 else 'an [[Rarity (BATTD)|uncommon]]'} [[bomb (BATTD)|]] [[weapon (BATTD)|]] in ''[[Bloons Adventure Time TD]]''.

==Strategy==
{{{{strategy needed}}}}

==Gallery==
{{{{image needed}}}}

==In other languages==
{{{{BATTD langs
|da   ={g(da,l)}
|de   ={g(de,l)}
|es   ={g(es,l)}
|fr   ={g(fr,l)}
|it   ={g(it,l)}
|ja   ={g(ja,l)}
|ko   ={g(ko,l)}
|nl   ={g(nl,l)}
|no   ={g(no,l)}
|pt-br={g(ptbr,l)}
|ru   ={g(ru,l)}
|sv   ={g(sv,l)}
|tr   ={g(tr,l)}
}}}}

==Navigation==
{{{{BATTD weapon navbox}}}}
{{{{-stop-}}}}
''')

f.close()
p.close()